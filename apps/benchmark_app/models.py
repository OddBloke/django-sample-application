# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    tags = models.ManyToManyField(Tag, related_name='articles',
                                  blank=True, null=True)


