from django.urls import path, re_path
from .views import del_comment


urlpatterns = [
    re_path(r'^delete/(?P<cid>[0-9]+)$', del_comment),
]

