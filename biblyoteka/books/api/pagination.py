from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    # page_size = 3
    page_size = 1
