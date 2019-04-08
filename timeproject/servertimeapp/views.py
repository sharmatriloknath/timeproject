from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def servertime(request):
    time="<h1>the current time of server:</h1>"
    time=time+str(datetime.datetime.now())
    return HttpResponse(time)
