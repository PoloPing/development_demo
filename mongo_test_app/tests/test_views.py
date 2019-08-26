from mongo_test_app.views import EntryViewSet
from mongo_test_app.models import Entry

from django.urls import reverse

import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews:

    def test_entry_create(self):
        user = mixer.blend('user.User')
        entry_data = {'author': user.id, 'blog': {'name': '123', 'tagline': '123'}, 'headline': 'JThyOXuGDkbVNeSqKrHQ'}
        view = EntryViewSet.as_view({'post': 'create'})
        factory = APIRequestFactory()
        path = reverse('entry-list')
        req = factory.post(path, data=entry_data, format='json')
        resp = view(req)

        assert Entry.objects.count() == 1
        assert resp.status_code == status.HTTP_201_CREATED

    def test_entry_list(self):
        entry_nums = 5
        user = mixer.blend('user.User')
        mixer.cycle(entry_nums).blend('mongo_test_app.Entry',
                                      author=user,
                                      blog={'name': '123', 'tagline': '123'},
                                      headline='JThyOXuGDkbVNeSqKrHQ')
        view = EntryViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()
        path = reverse('entry-list')
        req = factory.get(path, format='json')
        resp = view(req)
        assert len(resp.data) == entry_nums
        assert resp.status_code == status.HTTP_200_OK

    def test_entry_retrieve(self):
        user = mixer.blend('user.User')
        entry = mixer.blend('mongo_test_app.Entry',
                            author=user,
                            blog={'name': '123', 'tagline': '123'},
                            headline='JThyOXuGDkbVNeSqKrHQ')
        view = EntryViewSet.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()
        path = reverse('entry-detail', kwargs={'pk': entry.id})
        req = factory.get(path, format='json')
        resp = view(req, pk=entry.id)

        assert resp.status_code == status.HTTP_200_OK
        assert resp.data == {'author': user.id, 'blog': {'name': '123', 'tagline': '123'}, 'headline': 'JThyOXuGDkbVNeSqKrHQ'}

    def test_entry_update(self):
        user = mixer.blend('user.User')
        blog = {'name': '123', 'tagline': '123'}
        entry = mixer.blend('mongo_test_app.Entry',
                            author=user,
                            blog=blog,
                            headline='JThyOXuGDkbVNeSqKrHQ')
        factory = APIRequestFactory()
        view = EntryViewSet.as_view({'put': 'update'})
        path = reverse('entry-detail', kwargs={'pk': entry.id})
        req = factory.put(path, data={'author': user.id,
                                      'blog': {'name': '321', 'tagline': '321'},
                                      'headline': '777'},
                          format='json')
        resp = view(req, pk=entry.id)

        assert resp.status_code == status.HTTP_200_OK
        assert resp.data == {'author': user.id, 'blog': {'name': '321', 'tagline': '321'}, 'headline': '777'}

    def test_user_partial_update(self):
        user = mixer.blend('user.User')
        blog = {'name': '123', 'tagline': '123'}
        entry = mixer.blend('mongo_test_app.Entry',
                            author=user,
                            blog=blog,
                            headline='JThyOXuGDkbVNeSqKrHQ')
        view = EntryViewSet.as_view({'put': 'partial_update'})
        factory = APIRequestFactory()
        path = reverse('entry-detail', kwargs={'pk': entry.id})
        req = factory.put(path, data={'headline': '3333'}, format='json')
        resp = view(req, pk=entry.id)
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data['headline'] == '3333'

    def test_user_destroy(self):
        user = mixer.blend('user.User')
        blog = {'name': '123', 'tagline': '123'}
        entry = mixer.blend('mongo_test_app.Entry',
                            author=user,
                            blog=blog,
                            headline='JThyOXuGDkbVNeSqKrHQ')
        assert Entry.objects.count() == 1
        view = EntryViewSet.as_view({'delete': 'destroy'})
        factory = APIRequestFactory()
        path = reverse('entry-detail', kwargs={'pk': entry.id})
        req = factory.delete(path, format='json')
        resp = view(req, pk=entry.id)
        assert resp.status_code == status.HTTP_204_NO_CONTENT
        assert Entry.objects.count() == 0

