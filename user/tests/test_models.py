import pytest
from user.models import User
from django.contrib.auth.hashers import check_password

USERNAME = 'test_user'
EMAIL = ''
PASSWORD = 'pass1234'


@pytest.mark.django_db
class TestModels:
    def test_user_models(self):
        user = User.objects.create_user(USERNAME, EMAIL, PASSWORD)
        assert user.username == USERNAME
        assert user.email == EMAIL
        assert check_password(PASSWORD, user.password)
