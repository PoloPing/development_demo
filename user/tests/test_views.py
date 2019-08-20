from django.urls import reverse

from user.views import UserViewSet

import pytest
from rest_framework.test import APIRequestFactory
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews:

    def test_user_detail(self):
        view = UserViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': 1})
        req = factory.get(path, format='json')
        req.user = mixer.blend('user.User')
        resp = view(req)
        assert resp.status_code == 200

