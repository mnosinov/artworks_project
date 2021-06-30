from datetime import timedelta
from django.contrib import messages
from .models import Author, Genre, ArtworkType, Artwork, Book, Media


class InserDataHelper():
    def __init__(self, request):
        self.request = request

    def reset_data(self):
        insert_authors()
        cnt = Author.objects.count()
        messages.success(self.request, 'authors inserted ' + str(cnt))
        insert_genres()
        cnt = Genre.objects.count()
        messages.success(self.request, 'genres inserted ' + str(cnt))
        insert_artworks()
        cnt = Artwork.objects.count()
        messages.success(self.request, 'artworks inserted ' + str(cnt))


def insert_artworks():
    # clean the table
    Artwork.objects.all().delete()
    # insert data - Book
    genre = Genre.objects.filter(title='SciFi').first()
    author = Author.objects.filter(name='Glukhovsky').first()
    artwork = Artwork.objects.create(title='Metro 2033',
                                     type=ArtworkType.BOOK,
                                     genre=genre,
                                     author=author,
                                     pub_year=2005,
                                     price=10)
    Book.objects.create(artwork=artwork, pages=384)

    # insert data - Music
    genre = Genre.objects.filter(title='Blues').first()
    author = Author.objects.filter(name='Marvin').first()
    artwork = Artwork.objects.create(title='I Heard It Through The Grapevine',
                           type=ArtworkType.MUSIC,
                           genre=genre,
                           author=author,
                           pub_year=1968,
                           price=5)
    Media.objects.create(artwork=artwork, media_type=Media.Type.MUSIC,
                         duration=timedelta(minutes=3, seconds=24))


def insert_genres():
    # clean the table
    Genre.objects.all().delete()
    # insert data - Paining
    Genre.objects.create(title='History Painting',
                         artwork_type=ArtworkType.PAINTING)
    Genre.objects.create(title='Portrait',
                         artwork_type=ArtworkType.PAINTING)
    Genre.objects.create(title='Landscape',
                         artwork_type=ArtworkType.PAINTING)
    Genre.objects.create(title='Still Life',
                         artwork_type=ArtworkType.PAINTING)
    # insert data - Music
    Genre.objects.create(title='Classic',
                         artwork_type=ArtworkType.MUSIC)
    Genre.objects.create(title='Jazz',
                         artwork_type=ArtworkType.MUSIC)
    Genre.objects.create(title='Blues',
                         artwork_type=ArtworkType.MUSIC)
    # insert data - Movie
    Genre.objects.create(title='Horror',
                         artwork_type=ArtworkType.MOVIE)
    Genre.objects.create(title='Thriller',
                         artwork_type=ArtworkType.MOVIE)
    Genre.objects.create(title='Wild Life and Nature',
                         artwork_type=ArtworkType.MOVIE)
    # insert data - Book
    Genre.objects.create(title='Novel',
                         artwork_type=ArtworkType.BOOK)
    Genre.objects.create(title='SciFi',
                         artwork_type=ArtworkType.BOOK)
    Genre.objects.create(title='Photo Book',
                         artwork_type=ArtworkType.BOOK)
    Genre.objects.create(title='Science',
                         artwork_type=ArtworkType.BOOK)
    Genre.objects.create(title='Poetry',
                         artwork_type=ArtworkType.BOOK)


def insert_authors():
    # clean the table
    Author.objects.all().delete()
    # insert data
    Author.objects.create(name='Arthur')
    Author.objects.create(name='John')
    Author.objects.create(name='Marvin')
    Author.objects.create(name='Dave')
    Author.objects.create(name='Robert')
    Author.objects.create(name='Glukhovsky')
