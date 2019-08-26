from rest_framework import viewsets, mixins

from mongo_test_app.models import Entry
from mongo_test_app.serializers import EntrySerializer


class EntryViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    model = Entry
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    permission_classes = []
