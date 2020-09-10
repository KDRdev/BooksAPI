import csv
from django.core.management import BaseCommand
from books.models import Book, Rating

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            line_count = 0
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if line_count == 0:
                    line_count += 1
                else:
                    book = Book.objects.get(isbn=row[0])
                    rating = Rating.objects.create(
                        book=book,
                        rating=row[1],
                        review=row[2],
                    )
                    rating.save()
                    line_count += 1
                