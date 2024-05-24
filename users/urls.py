from django.urls import path,include
from . import views
from bookshop.views import index
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('users/register',views.register,name='register'),
    path('users/login',views.login,name='login'),
    path('users/dashboard', views.dashboard, name='dashboard'),
    path('users/logout', views.logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
