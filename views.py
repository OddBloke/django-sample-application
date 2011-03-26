# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def static(request):
    return render_to_response('static.html', {},
                              context_instance=RequestContext(request))


def simple_db_query(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def sequential_db_query(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def complex_db_query(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def db_write(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def upload(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


