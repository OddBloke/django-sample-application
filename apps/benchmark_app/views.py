# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from benchmark_app.models import Article
from benchmark_app.models import Tag

def home(request):
    # populate database with sample data
    for i in range(10):
        a = Article(
            title='test',
            text='test',
        )
        a.save()

    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def static(request):
    return render_to_response('benchmark_app/static.html', {},
                              context_instance=RequestContext(request))


def simple_db_query(request):
    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def sequential_db_query(request):
    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def complex_db_query(request):
    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def db_write(request):
    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def upload(request):
    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


