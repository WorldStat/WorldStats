from django.urls import path
from .views import main, about, contacts, feedback

urlpatterns = [
    path('', main, name = 'main'),
    path('about', about, name = 'about'),
    path('contacts', contacts, name = 'contacts'),
    path('feedback', feedback, name = 'feedback')
]