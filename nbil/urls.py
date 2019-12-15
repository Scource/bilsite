from django.urls import path

from . import views


app_name='nbil'
urlpatterns = [
    path('', views.index, name='index'),
    path('ur_list', views.ur_list, name='ur_list'),
    path('<int:detail_id>/', views.detail, name='detail'),
	path('<int:result_id>/check', views.results, name='check'),
    path('<int:UR>/voteeee', views.vote, name='vote'),


]