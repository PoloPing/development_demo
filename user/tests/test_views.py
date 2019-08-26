from user.views import UserViewSet
from user.models import User
from user.serializers import UserSerializer

from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.urls import reverse
import pytest
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
        assert User.objects.count() == 1
        assert resp.status_code == status.HTTP_201_CREATED

    def test_user_list(self):
        user_nums = 5
        mixer.cycle(user_nums).blend('user.User')
        view = UserViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()
        path = reverse('user-list')
        req = factory.get(path, format='json')
        resp = view(req)
        assert len(resp.data) == user_nums
        assert resp.status_code == status.HTTP_200_OK

    def test_user_retrieve(self):
        user = mixer.blend('user.User')
        view = UserViewSet.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': user.id})
        req = factory.get(path, format='json')
        resp = view(req, pk=user.id)
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data == user.to_dict(UserSerializer.Meta.fields)

    def test_user_update(self):
        user = mixer.blend('user.User')
        view = UserViewSet.as_view({'put': 'update'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': user.id})
        with mixer.ctx(commit=False):
            fake_user = mixer.blend('user.User')
            fake_user_data = fake_user.to_dict(['password', 'username', 'email'])
        req = factory.put(path, data=fake_user_data, format='json')
        resp = view(req, pk=user.id)
        resp_data = resp.data.copy()
        resp_data.pop('id')
        assert resp.status_code == status.HTTP_200_OK
        assert resp_data == fake_user_data

    def test_user_partial_update(self):
        user = mixer.blend('user.User')
        view = UserViewSet.as_view({'put': 'partial_update'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': user.id})
        req = factory.put(path, data={"email": "test@email.com"}, format='json')
        resp = view(req, pk=user.id)
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data['email'] == "test@email.com"

    def test_user_destroy(self):
        user = mixer.blend('user.User')
        assert User.objects.count() == 1
        view = UserViewSet.as_view({'delete': 'destroy'})
        factory = APIRequestFactory()
        path = reverse('user-detail', kwargs={'pk': user.id})
        req = factory.delete(path, format='json')
        resp = view(req, pk=user.id)
        assert resp.status_code == status.HTTP_204_NO_CONTENT
        assert User.objects.count() == 0

