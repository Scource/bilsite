from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import UR_objects, UR_conn



def index(request):
	ob_list = UR_objects.objects.all()[:6]
	context = {'kutasy': ob_list}
	return render(request, 'nbil/index.html', context)

# def detail(request, detail_id):
# 	ob=get_object_or_404(UR_objects, pk=detail_id)

# 	try 
# 		show=UR_objects.POB_id.get(pk.request.POST['data'])
# 	except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'ob': ob,
#             'error_message': "You didn't select a choice.",})

def detail(request, detail_id):
	ob = get_object_or_404(UR_objects, pk=detail_id)
	return render(request, 'nbil/detail.html', {'ob': ob})




def results(request, result_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(result_id))

def vote(request, UR):
    return HttpResponse("You're voting on question  {}".format(UR))