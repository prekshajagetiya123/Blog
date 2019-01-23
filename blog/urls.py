
from django.conf.urls import url

from .views import (
    ArticleListView,
    ArticleDetailView
)


app_name = 'articles'
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name = 'article-list'),
    url(r'^<int:pk>$', ArticleDetailView.as_view(), name = 'article-detail'),

]