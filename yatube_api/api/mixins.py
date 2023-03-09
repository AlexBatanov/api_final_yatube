from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import viewsets


class ListCreateViewSet(ListModelMixin, CreateModelMixin,
                        viewsets.GenericViewSet):
    pass
