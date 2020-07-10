from .views import register_view
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('register/', register_view, name='register'),
]