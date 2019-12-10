from django.urls import path

from . import views


app_name='nbil'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
	path('<int:UR>/results', views.results, name='result'),
    path('<int:UR>/voteeee', views.vote, name='vote'),


]