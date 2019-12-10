from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import UR_objects



def index(request):
	ob_list = UR_objects.objects.all()[:4]
	context = {'kutasy': ob_list}
	return render(request, 'nbil/index.html', context)

def detail(request, id):
	ob=get_object_or_404(UR_objects, pk=id)
	return render(request, 'nbil/detail.html', {'ob': ob})

def results(request, UR):
    response = "You're looking at the results of question {}.}"
    return HttpResponse(response.format(UR))

def vote(request, UR):
    return HttpResponse("You're voting on question  {}".format(UR))