# -*- coding: utf-8 -*-

import random

from django.conf import settings

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count, Max, Min, Sum
from django.db import transaction

from benchmark_app.models import Article
from benchmark_app.models import Tag

@transaction.commit_manually
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
                transaction.rollback()
            else:
                transaction.commit()

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

                try:
                    a.save()
                except:
                    transaction.rollback()
                else:
                    transaction.commit()


                # add random tags to article
                amount = random.randint(10, 30)
                for i in range(amount):
                    index = random.randint(0, Tag.objects.all().count()-1)
                    tag = Tag.objects.all()[index]
                    a.tags.add(tag)

                try:
                    a.save()
                except:
                    transaction.rollback()
                else:
                    transaction.commit()


    return render_to_response('benchmark_app/home.html', {},
                              context_instance=RequestContext(request))


def static(request):
    return render_to_response('benchmark_app/static.html', {},
                              context_instance=RequestContext(request))


def simple_db_query(request):
    """
    Simple DB Query

    Render a list of the 30 newest articles
    """
    articles = Article.objects.all().order_by('-created')

    if articles.count() > 30:
        articles = articles[0:30]

    context = {
        'articles': articles,
    }

    return render_to_response('benchmark_app/simple.html', context,
                              context_instance=RequestContext(request))


def complex_db_query(request):
    """
    Complex DB Query

    Render a list of the 30 most used tags that contain 'zz'
    """

    tags = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .filter(name__contains='zz') \
              .order_by('-num_of_articles')

    if tags.count() > 30:
        tags = tags[0:30]

    context = {
        'tags': tags
    }

    return render_to_response('benchmark_app/complex.html', context,
                              context_instance=RequestContext(request))


def sequential_db_query(request):
    """
    Runs a few of the complex queries in a row and displays the output
    """
    tags1 = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .filter(name__contains='zz') \
              .order_by('-num_of_articles')

    if tags1.count() > 30:
        tags1 = tags1[0:30]

    tags2 = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .order_by('num_of_articles')

    if tags2.count() > 30:
        tags2 = tags2[0:30]

    tags3 = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .order_by('-num_of_articles')

    if tags3.count() > 30:
        tags3 = tags3[0:30]

    tags4 = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .filter(name__contains='a') \
              .order_by('-name', 'created')

    if tags4.count() > 30:
        tags4 = tags4[0:30]

    tags5 = Tag.objects.select_related() \
              .annotate(num_of_articles=Count('articles')) \
              .filter(name__contains='zz') \
              .order_by('-created', 'name')

    if tags5.count() > 30:
        tags5 = tags5[0:30]

    articles = Article.objects.all().order_by('-created')

    if articles.count() > 30:
        articles = articles[0:30]


    context = {
        'tags1': tags1,
        'tags2': tags2,
        'tags3': tags3,
        'tags4': tags4,
        'tags5': tags5,
        'articles': articles,
    }

    return render_to_response('benchmark_app/sequential.html', context,
                              context_instance=RequestContext(request))


def db_write(request):
    """
    Adds a new random article to our database
    """
    amount = random.randint(0,6)

    str_list = []
    txt = ''
    while txt == '':
        index = random.randint(0, len(settings.TEST_DATA)-1)
        for i in range(amount):
            str_list.append(settings.TEST_DATA[index])
        txt = " ".join(str_list)

    a = None
    if txt != '':
        a = Article(
            title=txt[0:((index+1)*amount)],
            text=txt,
        )
        a.save()

        # add random tags to article
        amount = random.randint(10, 30)
        for i in range(amount):
            index = random.randint(0, Tag.objects.all().count()-1)
            tag = Tag.objects.all()[index]
            a.tags.add(tag)

        a.save()

    context = {
        'article': a,
        'count': Article.objects.all().count(),
    }

    return render_to_response('benchmark_app/write.html', context,
                              context_instance=RequestContext(request))


from benchmark_app.forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    """
    Takes a image as post parameter and stores it.
    """
    msg = ''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            destination = open('somefile.dat', 'wb+')
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)
            destination.close()
            msg = 'File uploaded successful.'
    else:
        form = UploadFileForm()

    context = {
        'form': form,
        'msg': msg,
    }

    return render_to_response('benchmark_app/upload.html', context,
                              context_instance=RequestContext(request))


