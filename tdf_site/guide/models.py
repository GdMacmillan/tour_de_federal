from django.contrib.postgres.fields import JSONField, ArrayField
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.db import models

class Restaraunt(models.Model):
    """Restaraunt Review"""
    formatted_address = models.CharField(max_length=100, blank=True, default='')
    geometry = JSONField()
    icon = models.URLField()
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    opening_hours = JSONField(null=True)
    photos = ArrayField(models.TextField(), null=True)
    place_id = models.CharField(max_length=100, blank=True, default='')
    price_level = models.PositiveSmallIntegerField(null=True)
    rating = models.PositiveSmallIntegerField()
    reference = models.CharField(max_length=200, blank=True, default='')
    types = ArrayField(models.CharField(max_length=100))
    review = RichTextField(default='')

    class Meta:
        verbose_name = 'Restaraunt'
        verbose_name_plural = 'Restaraunts'
