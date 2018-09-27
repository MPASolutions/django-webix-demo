# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django_webix.forms import WebixModelForm

from library.models import Author


class AuthorForm(WebixModelForm):
    class Meta:
        model = Author
        fields = '__all__'
