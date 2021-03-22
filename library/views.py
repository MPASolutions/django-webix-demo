# -*- coding: utf-8 -*-

from django.db.models import F, Value as V
from django.db.models.functions import Concat
from django.views.generic import TemplateView
from django_webix.forms import WebixTabularInlineFormSet
from django_webix.views import WebixListView, WebixCreateView, WebixUpdateView, WebixDeleteView

from library.forms import AuthorForm, BookForm
from library.models import Author, Book, Review


class HomeView(TemplateView):
    template_name = 'base.html'


class BookInline(WebixTabularInlineFormSet):
    model = Book
    fields = '__all__'


class AuthorListView(WebixListView):
    model = Author
    enable_json_loading = True
    fields = [
        {
            'field_name': 'id',
            'datalist_column': '''{id: "id", serverFilterType: "iexact", header: ["ID", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
        {
            'field_name': 'first_name',
            'datalist_column': '''{id: "first_name", serverFilterType: "icontains", header: ["First name", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
        {
            'field_name': 'last_name',
            'datalist_column': '''{id: "last_name", serverFilterType: "icontains", header: ["Last name", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
    ]


class AuthorCreateView(WebixCreateView):
    model = Author
    inlines = [BookInline]
    form_class = AuthorForm
    permissions = False
    model_copy_fields = ['first_name', 'last_name']
    inlines_copy_fields = {}


class AuthorUpdateView(WebixUpdateView):
    model = Author
    inlines = [BookInline]
    form_class = AuthorForm


class AuthorDeleteView(WebixDeleteView):
    model = Author
    nested_prevent = True


class ReviewInline(WebixTabularInlineFormSet):
    model = Review
    fields = '__all__'


class BookListView(WebixListView):
    model = Book
    enable_json_loading = True
    fields = [
        {
            'field_name': 'id',
            'datalist_column': '''{id: "id", serverFilterType: "iexact", header: ["ID", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
        {
            'field_name': 'title',
            'datalist_column': '''{id: "title", serverFilterType: "icontains", header: ["Title", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
        {
            'field_name': 'description',
            'datalist_column': '''{id: "description", serverFilterType: "icontains", header: ["Description", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
        {
            'field_name': 'author_fullname',
            'datalist_column': '''{id: "author_fullname", serverFilterType: "icontains", header: ["Author", {content: "serverFilter"}], fillspace: true, sort: "server"}'''
        },
    ]

    def get_initial_queryset(self):
        qs = super().get_initial_queryset()
        qs = qs.annotate(
            author_fullname=Concat(F('author__first_name'), V(" "), F('author__last_name'))
        )
        return qs


class BookCreateView(WebixCreateView):
    model = Book
    inlines = [ReviewInline]
    form_class = BookForm
    model_copy_fields = ['title', 'description', 'author']
    inlines_copy_fields = {}


class BookUpdateView(WebixUpdateView):
    model = Book
    inlines = [ReviewInline]
    form_class = BookForm


class BookDeleteView(WebixDeleteView):
    model = Book
