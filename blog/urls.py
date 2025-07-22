from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
