from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('tabletas/', views.search_department, name='search_department'),
    path('create/', views.create_tablet, name='create_tablet'),
    path('update/<int:pk>/', views.update_tablet, name='update_tablet'),
    path('delete/<int:pk>/', views.delete_tablet, name='delete_tablet'),
]