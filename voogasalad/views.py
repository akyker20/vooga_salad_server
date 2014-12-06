import json as simplejson
from django.shortcuts import render, redirect
from django.http import HttpResponse

def get_master_json(request):
	json = ['hello chase']
	return HttpResponse(simplejson.dumps(json), 
						content_type="application/json")
