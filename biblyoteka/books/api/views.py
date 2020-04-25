from rest_framework import generics, mixins
from biblyoteka.books import models
from . import serializers
from rest_framework.generics import get_object_or_404

# class EBookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#     queryset = models.EBook.objects.all()
#     serializer_class = serializers.EBookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class EBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EBook.objects.all()
    serializer_class = serializers.EBookSerializer

class EBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EBook.objects.all()
    serializer_class = serializers.EBookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(models.EBook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer









