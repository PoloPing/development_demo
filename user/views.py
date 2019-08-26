from rest_framework import viewsets, mixins

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []