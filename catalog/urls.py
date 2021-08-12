from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('index/', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),
     path('insertar/', views.insertar, name='insertar'),
      path('historial/', views.historial, name='historial'),
]