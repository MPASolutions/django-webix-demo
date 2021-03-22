# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include

from django_webix_demo import admin_webix
from library.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from library.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView
from library.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('django-webix/', include('django_webix.urls')),

    # Standard Django-Webix
    path('', HomeView.as_view(), name='home'),

    path('authors/list', AuthorListView.as_view(), name='library.author.list'),
    path('authors/create', AuthorCreateView.as_view(), name='library.author.create'),
    path('authors/update/<int:pk>', AuthorUpdateView.as_view(), name='library.author.update'),
    path('authors/delete/<int:pk>', AuthorDeleteView.as_view(), name='library.author.delete'),

    path('books/list', BookListView.as_view(), name='library.book.list'),
    path('books/create', BookCreateView.as_view(), name='library.book.create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='library.book.update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='library.book.delete'),

    # Admin Django-Webix
    path('webix-admin/', admin_webix.webix_site.urls),
]
