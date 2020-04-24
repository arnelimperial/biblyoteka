from django.urls import path
from . import views

app_name = "ebooks"
urlpatterns = [
    path("ebooks/", views.EBookListCreateAPIView.as_view(), name='ebook-list')
]
