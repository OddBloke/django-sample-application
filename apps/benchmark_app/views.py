# -*- coding: utf-8 -*-

import random

from django.conf import settings

from django.shortcuts import render_to_response
from django.template import RequestContext

from benchmark_app.models import Article
from benchmark_app.models import Tag

def home(request):
    if Article.objects.all().count() == 0:
        # extract all tags from test_data
        tags = []
        for line in settings.TEST_DATA:
            extracted_tags = list(set(line.split()))
            for t in extracted_tags:
                tags.append(t.replace(".", "").replace(",", ""))

        # populate database with tags
        for tag in tags:
            t = Tag(name=tag)
            try:
                t.save()
            except:
                pass

        # populate database with sample articles
        for i in range(1000):
            index = random.randint(0, len(settings.TEST_DATA)-1)
            amount = random.randint(0,6)

            str_list = []
            for i in range(amount):
                str_list.append(settings.TEST_DATA[index])
            txt = " ".join(str_list)

            if txt != '':
                a = Article(
                    title=txt[0:((index+1)*amount)],
                    text=txt,
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


