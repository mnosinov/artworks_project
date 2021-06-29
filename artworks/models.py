from django.db import models
from django_resized import ResizedImageField

from django.utils.translation import gettext as _


class Author(models.Model):
    name = models.CharField(max_length=100)


class ArtworkType(models.TextChoices):
    PAINTING = 'PAINTING', _('Painting')
    MUSIC = 'MUSIC', _('Music')
    MOVIE = 'MOVIE', _('Movie')
    BOOK = 'BOOK', _('BooK')


class Genre(models.Model):
    artwork_type = models.CharField(max_length=30, choices=ArtworkType.choices,
                                    null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)


class Artwork(models.Model):
    type = models.CharField(max_length=30, choices=ArtworkType.choices, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    pub_year = models.IntegerField(null=True, blank=True)


class Painting(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    # TODO TODO 
