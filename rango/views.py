# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'about_message': "About"}
    return render_to_response('rango/about.html', context_dict, context)
