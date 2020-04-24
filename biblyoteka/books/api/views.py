from rest_framework import generics, mixins
from biblyoteka.books import models
from . import serializers


class EBookListCreateAPIView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = models.EBook.objects.all()
    serializer_class = serializers.EBookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)






