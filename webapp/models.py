# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    img = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()

    # code = models.CharField(max_length=10)
    # description = models.CharField(max_length=200)
    # size = models.CharField(max_length=10)
    # color = models.CharField(max_length=20)

    def __str__(self):
        return self.title