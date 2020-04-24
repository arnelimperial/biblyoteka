from rest_framework import serializers
from biblyoteka.books import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"


class EBookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name=''
    # )

    class Meta:
        model = models.EBook
        fields = "__all__"
