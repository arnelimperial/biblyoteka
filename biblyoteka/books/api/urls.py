from django.urls import path
from . import views

app_name = "ebooks"
urlpatterns = [
    path("ebooks/",
         views.EBookListCreateAPIView.as_view(),
         name='ebook-list'),
    path("ebooks/<int:pk>/",
         views.EBookDetailAPIView.as_view(),
         name='ebook-detail'),
    path("ebooks/<int:ebook_pk>/review/",
         views.ReviewCreateAPIView.as_view(),
         name='ebook-review'),
    path("reviews/<int:pk>/",
         views.ReviewDetailAPIView.as_view(),
         name='review-detail'),


]
