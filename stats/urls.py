

from django.urls import path,re_path
from .views import index, create, delete, details, edit, details2


urlpatterns = [
    path('', index, name='stats/index'),
    path('create', create, name='stats/create'),
    path('delete', delete, name='stats/delete'),
    re_path(r'^details/(?P<article_id>[0-9]+)$', details),
    re_path(r'^details2/(?P<article_id>[0-9]+)$', details2),
    path('edit', edit, name='stats/edit')
]

