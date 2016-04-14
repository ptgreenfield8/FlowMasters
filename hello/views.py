from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Datapoint

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    datapoint = Datapoint(x=x, y=y)
    datapoint.save()

    datapoints = Datapoint.objects.all()

    return render(request, 'db.html', {'datapoints': datapoints})

def graph(request):

    datapoints = Datapoint.objects.all()

    return render(request, 'db.html', {'datapoints': datapoints})

def delete_db(request):
    confirm = request.GET.get('confirm')
    if (confirm == "yes"):
	DataPoint.objects.all().delete()
	return "Deleted"
    else:
	return "Not Deleted"
