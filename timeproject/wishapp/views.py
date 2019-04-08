from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    h=int(date.strftime("%H"))
    if h<12:
        msg='<h1> hi Good Morning </h1>'
        msg=msg+'str(date)'
    elif h<16:
        msg='<h1> hi good afternoon </h1>'
        msg=msg+str(date)
    elif h<21:
        msg='<h1> hi good evening </h1>'
        msg=msg+str(date)
    else:
        msg='<h1> hi good night </h1>'
        msg=msg+str(date)



    return HttpResponse(msg)
