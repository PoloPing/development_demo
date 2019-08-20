from djongo import models
from user.models import User


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    objects = models.DjongoManager()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name) + "-" + str(self.tagline)


class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_entries')
    blog = models.EmbeddedModelField(
        model_container=Blog
    )

    headline = models.CharField(max_length=255)
    objects = models.DjongoManager()


