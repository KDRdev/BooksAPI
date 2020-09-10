from django.db import models


class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    title = models.CharField('Tytuł', max_length=256)
    author = models.CharField('Autor', max_length=256)
    kind = models.CharField('Gatunek', max_length=256)
    
    def __str__(self):
        return self.title


class Rating(models.Model):
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        ], default=0)
    review = models.CharField('Opis', max_length=150)

    def __str__(self):
        return '%d: %s' % (self.rating, self.review)

