# -*- coding: utf-8 -*-

from django_webix.forms import WebixModelForm

from library.models import Author, Book


class AuthorForm(WebixModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(WebixModelForm):
    class Meta:
        model = Book
        fields = '__all__'
