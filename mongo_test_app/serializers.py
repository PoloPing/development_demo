from mongo_test_app.models import Entry
from rest_meets_djongo import serializers


class EntrySerializer(serializers.DjongoModelSerializer):

    class Meta:
        model = Entry
        fields = ('author', 'blog', 'headline', )
