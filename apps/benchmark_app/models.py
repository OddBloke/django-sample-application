# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, unique=True)



