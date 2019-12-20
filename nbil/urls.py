from django.urls import path

from . import views


app_name='nbil'
urlpatterns = [
    path('', views.index, name='index'),
    path('ur_list', views.ur_list, name='ur_list'),
    path('ur_list/edit<int:urid>/', views.edit, name='uredit'),
    path('ur_list/info<int:urid>/', views.info, name='urinfo'),
	path('<int:result_id>/check', views.results, name='check'),
    path('<int:UR>/voteeee', views.vote, name='vote'),


]