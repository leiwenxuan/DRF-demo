from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = "size"
    max_page_size = 4


# class MyPagination(pagination.LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 3


# class MyPagination(pagination.CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 2
#     ordering = '-id'
#     page_size_query_param = "size"
#     max_page_size = 3