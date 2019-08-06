# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.views.generic import TemplateView
from django_webix.formsets import WebixTabularInlineFormSet
from django_webix.views import WebixCreateWithInlinesUnmergedView, WebixUpdateWithInlinesView, WebixDeleteView

from library.forms import AuthorForm, BookForm
from library.models import Author, Book, Review


class HomeView(TemplateView):
    template_name = 'base.html'


class BookInline(WebixTabularInlineFormSet):
    model = Book
    fields = '__all__'


class AuthorListView(TemplateView):
    template_name = 'author_list.js'
    webix_view_id = 'content_top'

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['datalist'] = json.dumps([{
            'id': i.pk,
            'first_name': i.first_name,
            'last_name': i.last_name
        } for i in Author.objects.order_by('first_name', 'last_name')])
        return context


class AuthorCreateView(WebixCreateWithInlinesUnmergedView):
    model = Author
    inlines = [BookInline]
    form_class = AuthorForm
    webix_view_id = 'content_top'


class AuthorUpdateView(WebixUpdateWithInlinesView):
    model = Author
    inlines = [BookInline]
    form_class = AuthorForm
    webix_view_id = 'content_top'


class AuthorDeleteView(WebixDeleteView):
    model = Author
    nested_prevent = True
    webix_view_id = 'content_top'


class ReviewInline(WebixTabularInlineFormSet):
    model = Review
    fields = '__all__'


class BookListView(TemplateView):
    template_name = 'book_list.js'
    webix_view_id = 'content_bottom'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['datalist'] = json.dumps([{
            'id': i.pk,
            'title': i.title,
            'description': i.description,
            'author': '{}'.format(i.author)
        } for i in Book.objects.order_by('title')])
        return context


class BookCreateView(WebixCreateWithInlinesUnmergedView):
    model = Book
    inlines = [ReviewInline]
    form_class = BookForm
    webix_view_id = 'content_bottom'


class BookUpdateView(WebixUpdateWithInlinesView):
    model = Book
    inlines = [ReviewInline]
    form_class = BookForm
    webix_view_id = 'content_bottom'


class BookDeleteView(WebixDeleteView):
    model = Book
    webix_view_id = 'content_bottom'
