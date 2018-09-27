# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.views.generic import TemplateView
from django_webix.formsets import WebixTabularInlineFormSet
from django_webix.views import WebixCreateWithInlinesUnmergedView, WebixUpdateWithInlinesView, WebixDeleteView

from library.forms import AuthorForm
from library.models import Author, Book


class HomeView(TemplateView):
    template_name = 'base.html'


class BookInline(WebixTabularInlineFormSet):
    model = Book
    fields = '__all__'


class AuthorListView(TemplateView):
    template_name = 'author_list.js'

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


class AuthorUpdateView(WebixUpdateWithInlinesView):
    model = Author
    inlines = [BookInline]
    form_class = AuthorForm


class AuthorDeleteView(WebixDeleteView):
    model = Author
