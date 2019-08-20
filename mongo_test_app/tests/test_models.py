import pytest
from mixer.backend.django import mixer
from mongo_test_app.models import Entry


@pytest.mark.django_db
class TestModels:

    def test_entry_to_user(self):
        user = mixer.blend('user.User')
        entry = mixer.blend('mongo_test_app.Entry',
                            author=user,
                            blog={'name': 'test1', 'tagline': 'test2'},
                            headline='test3')
        assert user == entry.author

