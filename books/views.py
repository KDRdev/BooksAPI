from rest_framework import viewsets, filters
from .models import Book, Rating
from .serializers import BookSerializer, RatingSerializer


class BookViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer