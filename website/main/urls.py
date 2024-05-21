from django.urls import path
from . import views, forms

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.user_logout, name="logout"),
    path('main', views.main, name="main"),
    path('registration', views.registration, name="registration"),
]