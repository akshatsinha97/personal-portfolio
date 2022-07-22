from turtle import home
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = 'Site Administrator Login'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Hello Akshat! Welcome back'
urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('projects', views.projects),
    path('contact', views.contact)]