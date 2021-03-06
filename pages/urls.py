from django.urls import path
from . import views

# app_name = 'pages'
urlpatterns = [
    path('', views.home_page_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
