# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from django_webix.models import GenericModelWebix


class Author(GenericModelWebix):
    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last name'))

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    class WebixMeta:
        url_list = 'author_list'
        url_create = 'author_create'
        url_update = 'author_update'
        url_delete = 'author_delete'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    author = models.ForeignKey(Author, verbose_name=_('Author'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
