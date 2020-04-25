from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from biblyoteka.books import models
from . import serializers
from biblyoteka.books.api import permissions as api_permissions
from biblyoteka.books.api import pagination as api_pagination
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
    queryset = models.EBook.objects.all().order_by('id')
    serializer_class = serializers.EBookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [api_permissions.IsAdminUserOrReadOnly]
    pagination_class = api_pagination.SmallSetPagination

class EBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EBook.objects.all()
    serializer_class = serializers.EBookSerializer
    permission_classes = [api_permissions.IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(models.EBook, pk=ebook_pk)
        reviewer = self.request.user
        reviewer_queryset = models.Review.objects.filter(
            ebook=ebook,
            reviewer=reviewer
        )
        if reviewer_queryset.exists():
            raise ValidationError('Review entry already been created.')
        serializer.save(ebook=ebook, reviewer=reviewer)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [api_permissions.IsReviewerOrReadOnly]









