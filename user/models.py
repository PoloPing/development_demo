from django.db import models
from django.contrib.auth.models import AbstractUser
import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        in_db = 'mysql'



# Create your models here.
