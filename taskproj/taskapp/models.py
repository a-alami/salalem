# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

