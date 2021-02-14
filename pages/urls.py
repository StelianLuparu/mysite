from django.urls import path
from .views import AboutView
from . import views


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', AboutView.as_view()),
]
