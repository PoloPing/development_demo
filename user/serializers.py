from user.models import User

from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'email',)

    def validate(self, validated_data):
        return validated_data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)