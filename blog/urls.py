from django.urls import path
from . import views


urlpatterns = [
    # empty path means home
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
