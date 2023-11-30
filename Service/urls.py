from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('create_user/', views.create_user, name="home"),
    path('create_customer/', views.create_customer, name="home"),
    path('create_form/', views.create_form, name="home"),
    path('get_form/', views.get_form, name="home"),
    path('get_forms/', views.get_forms, name="home"),
    path('delete_form/', views.delete_form, name="home"),
    path('delete_forms/', views.delete_forms, name="home"),
    path('add_query/', views.add_query, name="home"),
    path('add_response/', views.add_response, name="home"),
    path('get_query/', views.get_query, name="home"),
    path('get_queries/', views.get_queries, name="home"),
]