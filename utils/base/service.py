from typing import Any, List, Type, Union


class BaseService:
    result: Any = None
    errors: List[Exception]

    def __init__(self) -> None:
        self.errors = []

    def with_error(self, errors: Union[Exception, List[Exception], str]) -> Type['BaseService']:
        if isinstance(errors, Exception):
            self.errors.append(errors)
        elif isinstance(errors, List) and isinstance(errors[0], Exception):
            self.errors += errors
        elif isinstance(errors, str):
            self.errors.append(Exception(errors))
        return self