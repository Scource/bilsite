from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from .models import UR_objects, UR_conn
from .forms import Conn_form, edit_form


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
		form=edit_form(request.POST, instance=ob)
		if form.is_valid():
			form.save()
			return redirect('nbil:ur_list')
	else:
		form=edit_form(instance=ob)
	context={'form':form, 'ob':ob}
	return render(request, 'nbil/edit.html', context)

def info(request, urid):
	element=get_object_or_404(UR_objects, id=urid)
	conns=get_list_or_404(UR_conn, POB_id=urid)
	context={'element':element, 'conns':conns}
	return render(request, 'nbil/info.html', context)


def results(request, result_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(result_id))

def vote(request, UR):
    return HttpResponse("You're voting on question  {}".format(UR))