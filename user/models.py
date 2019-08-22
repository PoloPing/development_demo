from django.contrib.auth.models import AbstractUser
from development_demo.libs.models import ModelSerializeMixin


class User(AbstractUser, ModelSerializeMixin):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'




# Create your models here.
