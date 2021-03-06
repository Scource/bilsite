from django.urls import path

from . import views


app_name='nbil'
urlpatterns = [
    path('', views.index, name='index'),

    path('ur_list', views.ur_list, name='ur_list'),
    path('ur_list/edit<int:urid>/', views.edit, name='uredit'),
    path('ur_list/info<int:urid>/', views.info, name='urinfo'),
    path('ur_list/create_UR/', views.UR_create, name='urcreate'),

	path('conn_list/', views.connlist, name='connlist'),
    path('conn_list/edit<int:urid>/', views.connedit, name='connedit'),
    path('conn_list/create_conn/', views.createconn, name='conncreate'),


    path('tariff/', views.add_tariff, name='tariff'),
    path('zone/', views.add_zone, name='zone'),
    path('CSB_import/', views.add_CSB_data, name='CSB_import'),
    path('CSPR_data/', views.get_skome_data, name='CSPRdata'),


]