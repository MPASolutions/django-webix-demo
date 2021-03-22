# -*- coding: utf-8 -*-

from django_dal.params import ContextParam, ContextParams
from django.contrib.auth import get_user_model


class MyContextParams(ContextParams):
    params = [
        ContextParam('user', get_user_model(), 'Django User object'),
    ]

    def get_from_request(self, request):
        data = {
            'user': None,
        }
        if request.user.is_authenticated:
            data.update({
                'user': request.user,
            })
        return data
