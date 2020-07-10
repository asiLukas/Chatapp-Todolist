from .views import list_view, create_view, detail_view, update_view, delete_view
from django.urls import path

app_name = 'todolist'

urlpatterns = [
   path('create/', create_view, name='create_list'),
   path('', list_view, name='view_list'),
   path('detail/<int:id>', detail_view, name='detail_list'),
   path('update/<int:id>', update_view, name='update'),
   path('delete/<int:id>', delete_view, name='delete'),


]
