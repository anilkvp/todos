"""
todos item urls
"""
from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('details/<int:item_id>/', views.details, name='details'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]
