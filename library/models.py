# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext as _
from django_webix.models import GenericModelWebix


@python_2_unicode_compatible
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

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Author'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return '{author}, {title}'.format(author=self.author, title=self.title)
