from user.models import User
from rest_framework import serializers
from mongo_test_app.serializers import EntrySerializer


class UserSerializer(serializers.ModelSerializer):

    user_entries = EntrySerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'user_entries', )
