from django.urls import reverse

from user.views import UserViewSet
from user.models import User
import pytest
from rest_framework.test import APIRequestFactory
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews:

    def test_user_create(self):
        view = UserViewSet.as_view({'post': 'create'})
        factory = APIRequestFactory()
        path = reverse('user-list')
        with mixer.ctx(commit=False):
            user = mixer.blend('user.User')
            user_data = user.to_dict()
        req = factory.post(path, data=user_data, format='json')
        resp = view(req)
        assert resp.status_code == 201

    def test_user_retrieve(self):
        view = UserViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': 1})
        req = factory.get(path, format='json')
        req.user = mixer.blend('user.User')
        resp = view(req)
        assert resp.status_code == 200

    # def test_user_list(self):
    #     view = UserViewSet.as_view({'get': 'list'})
    #     factory = APIRequestFactory()
    #     path = reverse('user-detail', kwargs={'pk': 1})
    #     req = factory.get(path, format='json')
    #     req.user = mixer.blend('user.User')
    #     resp = view(req)
    #     assert resp.status_code == 200
    #
    # def test_user_update(self):
    #     view = UserViewSet.as_view({'put': 'update'})
    #     factory = APIRequestFactory()
    #     path = reverse('user-detail', kwargs={'pk': 1})
    #     req = factory.get(path, format='json')
    #     req.user = mixer.blend('user.User')
    #     resp = view(req)
    #     assert resp.status_code == 200
    #
    # def test_user_partial_update(self):
    #     view = UserViewSet.as_view({'put': 'update'})
    #     factory = APIRequestFactory()
    #     path = reverse('user-detail', kwargs={'pk': 1})
    #     req = factory.get(path, format='json')
    #     req.user = mixer.blend('user.User')
    #     resp = view(req)
    #     assert resp.status_code == 200
    #
    # def test_user_destroy(self):
    #     view = UserViewSet.as_view({'get': 'list'})
    #     factory = APIRequestFactory()
    #     path = reverse('user-detail', kwargs={'pk': 1})
    #     req = factory.get(path, format='json')
    #     req.user = mixer.blend('user.User')
    #     resp = view(req)
    #     assert resp.status_code == 200

