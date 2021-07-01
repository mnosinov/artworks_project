import os
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.forms.models import model_to_dict
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from formtools.wizard.views import SessionWizardView

from .insertdatahelper import InserDataHelper
from .models import Genre, Author, Artwork, ArtworkType, Painting, Media, Book
from . import forms


def index(request):
    return render(request, 'artworks/index.html')


class InsertSampleDataView(View):
    def get(self, request, *args, **kwargs):
        InserDataHelper(request).reset_data()
        messages.success(request,
                         'Sample Data have been successfully inserted.')
        return redirect('index')


# Genre -----------------------------------------------
class GenreListView(ListView):
    model = Genre


class GenreDetailView(DetailView):
    model = Genre


class GenreCreateView(CreateView):
    model = Genre
    fields = ('title', 'artwork_type')
    success_url = reverse_lazy('genres')


class GenreUpdateView(UpdateView):
    model = Genre
    fields = ('title', 'artwork_type')
    success_url = reverse_lazy('genres')


class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy('genres')


# Author -----------------------------------------------
class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    fields = ('name',)
    success_url = reverse_lazy('authors')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ('name',)
    success_url = reverse_lazy('authors')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


# Art Work -----------------------------------------------
class ArtworkListView(ListView):
    model = Artwork


class ArtworkDetailView(DetailView):
    model = Artwork


class ArtworkUpdateView(UpdateView):
    model = Artwork
    fields = ('name',)
    success_url = reverse_lazy('artworks')


class ArtworkDeleteView(DeleteView):
    model = Artwork
    success_url = reverse_lazy('artworks')


# multistep wizard form for artwork -----------------------------------------------
class ArtworkWizard(SessionWizardView):
    # form_list = [
    #     ArtworkForm1,
    #     ArtworkPaintingForm2, ArtworkBookForm2, ArtworkMovieForm2, ArtworkMusicForm2,
    # ]
    # template_name = 'artworks/artwork_wizard_single_unified_template.html'

    # forms
    FORMS = [

        ("form1", forms.ArtworkForm1),
        ("painting_form2", forms.ArtworkPaintingForm2),
        ("painting_form3", forms.ArtworkPaintingForm3),
        ("painting_form4", forms.ArtworkPaintingForm4),
        ("painting_form5", forms.ArtworkPaintingForm5),
        ("music_form2", forms.ArtworkMusicForm2),
        ("music_form3", forms.ArtworkMusicForm3),
        ("music_form4", forms.ArtworkMusicForm4),
        ("movie_form2", forms.ArtworkMovieForm2),
        ("movie_form3", forms.ArtworkMovieForm3),
        ("movie_form4", forms.ArtworkMovieForm4),
        ("book_form2", forms.ArtworkBookForm2),
        ("book_form3", forms.ArtworkBookForm3),
        ("book_form4", forms.ArtworkBookForm4),
        ("book_form5", forms.ArtworkBookForm5),
    ]
    # form templates
    TEMPLATES = {
        "form1": "artworks/artwork_wizard/form1.html",
        "painting_form2": "artworks/artwork_wizard/painting_form2.html",
        "painting_form3": "artworks/artwork_wizard/painting_form3.html",
        "painting_form4": "artworks/artwork_wizard/painting_form4.html",
        "painting_form5": "artworks/artwork_wizard/painting_form5.html",
        "music_form2": "artworks/artwork_wizard/music_form2.html",
        "music_form3": "artworks/artwork_wizard/music_form3.html",
        "music_form4": "artworks/artwork_wizard/music_form4.html",
        "movie_form2": "artworks/artwork_wizard/movie_form2.html",
        "movie_form3": "artworks/artwork_wizard/movie_form3.html",
        "movie_form4": "artworks/artwork_wizard/movie_form4.html",
        "book_form2": "artworks/artwork_wizard/book_form2.html",
        "book_form3": "artworks/artwork_wizard/book_form3.html",
        "book_form4": "artworks/artwork_wizard/book_form4.html",
        "book_form5": "artworks/artwork_wizard/book_form5.html",
    }
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'book_covers'))

    # conditions 
    def is_painting(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('form1') or {'type': 'NONE'}
        return cleaned_data['type'] == ArtworkType.PAINTING

    def is_music(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('form1') or {'type': 'NONE'}
        return cleaned_data['type'] == ArtworkType.MUSIC

    def is_movie(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('form1') or {'type': 'NONE'}
        return cleaned_data['type'] == ArtworkType.MOVIE

    def is_book(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('form1') or {'type': 'NONE'}
        return cleaned_data['type'] == ArtworkType.BOOK

    condition_dict = {
        "painting_form2": is_painting,
        "painting_form3": is_painting,
        "painting_form4": is_painting,
        "painting_form5": is_painting,
        "music_form2": is_music,
        "music_form3": is_music,
        "music_form4": is_music,
        "movie_form2": is_movie,
        "movie_form3": is_movie,
        "movie_form4": is_movie,
        "book_form2": is_book,
        "book_form3": is_book,
        "book_form4": is_book,
        "book_form5": is_book,
    }

    def get_template_names(self):
        return [ArtworkWizard.TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        if 'pk' in self.kwargs:
            artwork_id = self.kwargs['pk']
            if step in ('form1', 'painting_form2', 'painting_form5', 'music_form2',
                        'movie_form2', 'book_form2', 'music_form4', 'movie_form4',
                        'book_form5'):
                artwork = Artwork.objects.get(pk=artwork_id)
                return model_to_dict(artwork)
            elif step in ('painting_form3', 'painting_form4'):
                painting = Painting.objects.get(pk=artwork_id)
                return model_to_dict(painting)
            elif step in ('music_form3', 'movie_form3'):
                media = Media.objects.get(pk=artwork_id)
                return model_to_dict(media)
            elif step in ('book_form3', 'book_form4'):
                book = Book.objects.get(pk=artwork_id)
                return model_to_dict(book)
            else:
                return self.initial_dict.get(step, {})
        else:
            return self.initial_dict.get(step, {})

    def done(self, form_list, form_dict, **kwargs):
        # save data from all of the steps
        artwork_type = form_dict['form1'].cleaned_data['type']

        artwork = Artwork(
            type=artwork_type,
            author=form_dict['form1'].cleaned_data['author'],
            title=form_dict['form1'].cleaned_data['title'],
            pub_year=form_dict['form1'].cleaned_data['pub_year'],
        )
        # if pk exists then it is UPDATE mode
        if 'pk' in self.kwargs:
            artwork.id = self.kwargs['pk']

        artwork.save()

        if artwork_type == ArtworkType.PAINTING:
            genre = form_dict['painting_form2'].cleaned_data['genre']
            price = form_dict['painting_form5'].cleaned_data['price']

            painting = Painting(
                artwork=artwork,
                height=form_dict['painting_form3'].cleaned_data['height'],
                width=form_dict['painting_form3'].cleaned_data['width'],
                paint=form_dict['painting_form4'].cleaned_data['paint'],
            )
            painting.save()
            success_message = 'Painting successfully saved.'
        elif artwork_type == ArtworkType.MUSIC:
            genre = form_dict['music_form2'].cleaned_data['genre']
            price = form_dict['music_form4'].cleaned_data['price']

            music = Media(
                artwork=artwork,
                media_type=Media.Type.MUSIC,
                duration=form_dict['music_form3'].cleaned_data['duration'],
            )
            music.save()
            success_message = 'Music successfully saved.'
        elif artwork_type == ArtworkType.MOVIE:
            genre = form_dict['movie_form2'].cleaned_data['genre']
            price = form_dict['movie_form4'].cleaned_data['price']

            movie = Media(
                artwork=artwork,
                media_type=Media.Type.VIDEO,
                duration=form_dict['movie_form3'].cleaned_data['duration'],
            )
            movie.save()
            success_message = 'Movie successfully saved.'
        elif artwork_type == ArtworkType.BOOK:
            genre = form_dict['book_form2'].cleaned_data['genre']
            price = form_dict['book_form5'].cleaned_data['price']

            book = Media(
                artwork=artwork,
                pages=form_dict['book_form3'].cleaned_data['pages'],
                cover=form_dict['book_form4'].cleaned_data['cover'],
            )
            book.save()
            success_message = 'Book successfully saved.'

        artwork.genre = genre
        artwork.price = price
        artwork.save()

        messages.success(self.request, success_message)
        return redirect('artworks')
