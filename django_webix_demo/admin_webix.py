# -*- coding: utf-8 -*-

from django.apps import apps
from django.conf import settings
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string


class AdminWebixSite(LazyObject):
    def _setup(self):

        AdminWebixSiteClass = import_string(apps.get_app_config('admin_webix').default_site)

        def extra_index_context(self, request):
            context = {
                'DEBUG': settings.DEBUG,
            }
            return context

        def dashboard(self, request, extra_context=None):
            context = {}

            from django.views.generic import TemplateView
            defaults = {
                'extra_context': {**self.each_context(request), **(extra_context or {}), **context},
            }
            if self.dashboard_template is not None:
                defaults['template_name'] = self.dashboard_template

            return TemplateView.as_view(**defaults)(request)

        AdminWebixSiteClass.extra_index_context = extra_index_context
        AdminWebixSiteClass.site_title = "Django Webix DEMO"
        AdminWebixSiteClass.index_title = "Django Webix DEMO"
        AdminWebixSiteClass.dashboard = dashboard

        self._wrapped = AdminWebixSiteClass()


webix_site = AdminWebixSite()
