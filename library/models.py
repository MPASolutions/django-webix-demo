# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _
from django_dal.models import DALModel


class Author(DALModel):
    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last name'))

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    @staticmethod
    def autocomplete_search_fields():
        return "first_name__icontains", "last_name__icontains",


class Book(DALModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Author'))
    cover = models.FileField(max_length=255, blank=True, null=True, verbose_name=_('Cover'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return '{author}, {title}'.format(author=self.author, title=self.title)

    @staticmethod
    def autocomplete_search_fields():
        return "title__icontains", "description__icontains", "author__first_name__icontains", \
               "author__last_name__icontains",


class Review(DALModel):
    comment = models.TextField(verbose_name=_('Comment'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('Book'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return '{book}, {comment}'.format(book=self.book, comment=self.comment)
