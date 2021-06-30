from django.db import models
from django_resized import ResizedImageField

from django.utils.translation import gettext as _


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ArtworkType(models.TextChoices):
    PAINTING = 'PAINTING', _('Painting')
    MUSIC = 'MUSIC', _('Music')
    MOVIE = 'MOVIE', _('Movie')
    BOOK = 'BOOK', _('BooK')


class Genre(models.Model):
    artwork_type = models.CharField(max_length=30, choices=ArtworkType.choices)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Artwork(models.Model):
    # type is mandatory field
    type = models.CharField(max_length=30, choices=ArtworkType.choices)
    # genre can be unknown - null
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    pub_year = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Painting(models.Model):
    artwork = models.OneToOneField(Artwork, on_delete=models.CASCADE, primary_key=True)
    height = models.IntegerField()
    width = models.IntegerField()
    paint = models.CharField(max_length=30)

    def __str__(self):
        return 'paining' + self.artwork.title


class Book(models.Model):
    artwork = models.OneToOneField(Artwork, on_delete=models.CASCADE, primary_key=True)
    pages = models.IntegerField()
    cover = ResizedImageField(upload_to='books/covers/%Y/%m/%d')

    def __str__(self):
        return 'book ' + self.artwork.title


class Media(models.Model):
    class MediaType(models.TextChoices):
        MUSIC = 'MUSIC', _('Music')
        VIDEO = 'VIDEO', _('Video')
    artwork = models.OneToOneField(Artwork, on_delete=models.CASCADE, primary_key=True)
    media_type = models.CharField(max_length=10, choices=MediaType.choices)
    duration = models.DurationField()

    def __str__(self):
        return 'media ' + self.media_type + ' ' + self.artwork.title
