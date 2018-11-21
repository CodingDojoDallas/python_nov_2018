from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<str:number>', views.number, name='number'),
    path('<str:number>/edit', views.edit, name='edit'),
    path('<str:number>/delete', views.destroy, name='delete')
]

