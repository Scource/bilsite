from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from .models import UR_objects, UR_conn
from .forms import Conn_form, UR_edit_form, conn_edit_form


def index(request):
	ob_list = UR_objects.objects.all()[:6]
	context = {'kutasy': ob_list}
	return render(request, 'nbil/index.html', context)

def ur_list(request):
	urlist=get_list_or_404(UR_objects)

	if request.method=='POST':
		form=Conn_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('nbil:ur_list')
	else:
		form=Conn_form()
	context={'form':form, 'urlist':urlist}
	return render(request, 'nbil/ur_list.html', context)


def edit(request, urid):
	ob = get_object_or_404(UR_objects, pk=urid)
	if request.method=='POST':
		form=UR_edit_form(request.POST, instance=ob)
		if form.is_valid():
			form.save()
			return redirect('nbil:ur_list')
	else:
		form=UR_edit_form(instance=ob)
	context={'form':form, 'ob':ob}
	return render(request, 'nbil/uredit.html', context)

def info(request, urid):
	element=get_object_or_404(UR_objects, id=urid)
	#conns=get_list_or_404(UR_conn, POB_id=urid)
	connspob=UR_conn.objects.filter(POB_id=urid)
	connsse=UR_conn.objects.filter(SE_id=urid)
	context={'element':element, 'connspob':connspob, 'connsse':connsse}
	return render(request, 'nbil/info.html', context)


def connlist(request):
    lista = get_list_or_404(UR_conn)
    context={'lista':lista}
    return render(request, 'nbil/connlist.html', context)

def connedit(request, urid):
	ob = get_object_or_404(UR_conn, pk=urid)
	if request.method=='POST':
		form=conn_edit_form(request.POST, instance=ob)
		if form.is_valid():
			form.save()
			return redirect('nbil:ur_list')
	else:
		form=conn_edit_form(instance=ob)
	context={'form':form, 'ob':ob}
	return render(request, 'nbil/connedit.html', context)


def createconn(request):
	if request.method=='POST':
		form=Conn_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('nbil:connlist')
	else:
		form=Conn_form()
	context={'form':form}
	return render(request, 'nbil/conncreate.html', context)