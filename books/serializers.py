from .models import Book, Rating
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'