from django.core.paginator import Paginator, EmptyPage


class APIPagination:
    instance: any
    total_rows: int
    page: int
    limit: int
    total_page: int

    def __init__(self, instance: any, page: int, limit: int) -> None:
        self.instance = instance; self.page = page; self.limit = limit

    @property
    def paginated_data(self) -> any:
        paginator = Paginator(self.instance, self.limit)
        self.total_rows = paginator.count
        self.total_page = paginator.num_pages
        try:
            paginated_data = paginator.page(self.page).object_list
            return paginated_data
        except EmptyPage: return []

    def _to_dict(self) -> dict:
        return {
            'page': self.page,
            'limit': self.limit,
            'totalPage': self.total_page,
            'totalRows': self.total_rows
        }