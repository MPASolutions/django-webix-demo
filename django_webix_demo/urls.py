"""django_webix_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from library.views import HomeView, AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    url(r'^django-webix/', include('django_webix.urls')),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^authors/list$', AuthorListView.as_view(), name='author_list'),
    url(r'^authors/create$', AuthorCreateView.as_view(), name='author_create'),
    url(r'^authors/update/(?P<pk>\d+)$', AuthorUpdateView.as_view(), name='author_update'),
    url(r'^authors/delete/(?P<pk>\d+)$', AuthorDeleteView.as_view(), name='author_delete'),
]
