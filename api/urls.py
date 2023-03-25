from django.urls import path

from .views import (
    home,

    NewsListAPIView,
    NewsCreateAPIView,
    NewsDetailAPIView,
    NewsUpdateAPIView,
    NewsDeleteAPIView
)

urlpatterns = [
    path("", home, name='home'),

    path("news/", NewsListAPIView.as_view(), name="news"),
    path("news/create/", NewsCreateAPIView.as_view(), name="create-news"),
    path("news/<int:pk>/", NewsDetailAPIView.as_view(), name="news"),
    path("news/update/<int:pk>/", NewsUpdateAPIView.as_view(), name="update-news"),
    path("news/delete/<int:pk>/", NewsDeleteAPIView.as_view(), name="delete-news")
]
