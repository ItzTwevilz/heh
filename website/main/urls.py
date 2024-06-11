from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.user_logout, name="logout"),
    path('main', views.main, name="main"),
    path('registration', views.registration, name="registration"),
    path('search', views.search_page, name='search'),
    path('show/<abb_id>', views.show_abb, name='show'),
    path('delete/<abb_id>', views.delete, name='delete'),
    path('update/<abb_id>', views.update, name='update'),
]