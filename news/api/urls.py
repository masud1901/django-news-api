from django.urls import path
from news.api.views import article_list_create_api_view, article_detail_api_view

from news.api.views import (
    ArticleDetailAPIView,
    ArticleListCreateAPIView,
    ReporterListCreateAPIView,
)

urlpatterns = [
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("reporters/", ReporterListCreateAPIView.as_view(), name="reporter-list"),
]
