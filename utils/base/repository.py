import logging
from typing import Optional, Union
from django.db import models, transaction



class BaseRepository:
    log: logging.Logger = logging.getLogger()
    main_model: models.Model
    queryset: models.QuerySet[models.Model]

    def __init__(self, qs: Optional[models.QuerySet] = None) -> None:
        self.queryset = qs or self.main_model.objects

    def with_filter(self, *args, **kwargs) -> "BaseRepository":
        self.queryset = self.queryset.filter(*args, **kwargs)
        return self

    def find_one(self, except_not_found: bool = False, *args, **filters) -> Union[models.Model, None]:
        try:
            result = self.queryset.get(*args, **filters)
            return result
        except self.main_model.DoesNotExist as err:
            if except_not_found:
                raise Exception(f"No {self.main_model._meta.db_table} data found")
        except Exception as err:
            self.log.exception(msg=f"{self.__class__.__name__}.find_one Exception: {str(err)}", stack_info=True)
            raise err

    def find_many(self, raise_exception: bool = True, *args, **filters) -> Optional[models.QuerySet[models.Model]]:
        try:
            results = self.queryset.filter(*args, **filters)
            return results
        except Exception as err:
            if raise_exception:
                raise err
            self.log.error(msg=f"{self.__class__.__name__}.find_many Exception: {str(err)}", stack_info=True)

    def create_one(self, raise_exception: bool = True, *args, **kwargs) -> models.Model:
        try:
            result = self.main_model(*args, **kwargs)
            result.save()
            return result
        except Exception as err:
            if raise_exception:
                raise err
            self.log.error(msg=f"{self.__class__.__name__}.create_one Exception: {str(err)}", stack_info=True)

    def update(self, *args, **kwargs) -> bool:
        try:
            self.queryset.update(*args, **kwargs)
            return True
        except Exception as err:
            self.log.error(msg=f"{self.__class__.__name__}.update_one Exception: {str(err)}", stack_info=True)
            return False

    def update_one(self, old_data: models.Model, raise_exception: bool = True, **new_data) -> Optional[models.Model]:
        try:
            self.queryset.filter(id=old_data.id).update(**new_data)
            return self.queryset.get(id=old_data.id)
        except Exception as err:
            if raise_exception:
                raise err
            self.log.error(msg=f"{self.__class__.__name__}.update_one Exception: {str(err)}", stack_info=True)

    def update_many(self, objects: models.QuerySet[models.Model], raise_exception: bool = True, *args, **new_data) -> Optional[models.QuerySet[models.Model]]:
        try:
            with transaction.atomic():
                objects.update(*args, **new_data)
                return objects
        except Exception as err:
            if raise_exception:
                raise err
            self.log.error(msg=f"{self.__class__.__name__}.update_many Exception: {str(err)}", stack_info=True)