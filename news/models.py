# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class NewsComment(models.Model):
    id = models.IntegerField(primary_key=True)
    newsid = models.IntegerField()
    name = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_comment'


class Newsmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    filepath = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsmodel'
