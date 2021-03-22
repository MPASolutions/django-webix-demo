# -*- coding: utf-8 -*-

from django.db.models import F, Value as V
from django.db.models.functions import Concat
from django_webix import admin_webix as admin
from django_webix.forms import WebixTabularInlineFormSet

from django_webix_demo.admin_webix import webix_site
from library.forms import BookForm, AuthorForm
from library.models import Author, Book, Review


class BookInline(WebixTabularInlineFormSet):
    model = Book
    fields = '__all__'

    factory_kwargs = {'extra': 0}


@admin.register(Author, site=webix_site)
class AuthorAdmin(admin.ModelWebixAdmin):
    list_display = ['id', 'first_name', 'last_name']
    inlines = [BookInline]
    form = AuthorForm
    enable_json_loading = True
    enable_column_copy = False


class ReviewInline(WebixTabularInlineFormSet):
    model = Review
    fields = '__all__'

    factory_kwargs = {'extra': 0}


@admin.register(Book, site=webix_site)
class BookAdmin(admin.ModelWebixAdmin):
    list_display = ['id', 'title', 'description', 'author_fullname']
    inlines = [ReviewInline]
    form = BookForm
    enable_json_loading = True
    enable_column_copy = False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            author_fullname=Concat(F('author__first_name'), V(" "), F('author__last_name'))
        )
        return qs
