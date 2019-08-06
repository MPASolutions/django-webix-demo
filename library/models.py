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
class Book(GenericModelWebix):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Author'))
    cover = models.FileField(max_length=255, blank=True, null=True, verbose_name=_('Cover'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    class WebixMeta:
        url_list = 'book_list'
        url_create = 'book_create'
        url_update = 'book_update'
        url_delete = 'book_delete'

    def __str__(self):
        return '{author}, {title}'.format(author=self.author, title=self.title)


@python_2_unicode_compatible
class Review(models.Model):
    comment = models.TextField(verbose_name=_('Comment'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('Book'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return '{book}, {comment}'.format(book=self.book, comment=self.comment)
