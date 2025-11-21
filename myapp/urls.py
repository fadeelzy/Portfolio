from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact_view, name='contact'),
]
