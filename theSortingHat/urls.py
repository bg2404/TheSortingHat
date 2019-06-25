from django.urls import re_path, path
from . import views
from django.views.generic import RedirectView

app_name = 'theSortingHat'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', RedirectView.as_view(url='/')),
    path('add/', views.create_student, name='create_student'),
    path('detail/', views.detail, name='detail'),
    path('sort/', views.sort, name='sort'),
]
