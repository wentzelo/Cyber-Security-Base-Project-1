from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_entry, name='add_entry'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]