from django.shortcuts import render
from django.http import HttpResponse
import datetime

def normal(request):
	now = datetime.datetime.now()
	html = "<html><p>this is now %s.</p></html>" % now 
	return HttpResponse(html)
# Create your views here.
