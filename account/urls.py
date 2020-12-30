from django.urls import path
from .views import entry, exit, profile, reg, ajax_reg

urlpatterns = [
    path('entry', entry, name='entry'),
    path('exit', exit, name='exit'),
    path('profile', profile, name='profile'),
    path('reg', reg, name='reg'),
    path('ajax_reg', ajax_reg, name='ajax_reg')
]