from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from formtools.wizard.views import SessionWizardView

from .insertdatahelper import InserDataHelper
from .models import Genre, Author, Artwork
from .forms import ArtworkForm1, \
    ArtworkPaintingForm2, ArtworkBookForm2, ArtworkMovieForm2, ArtworkBookForm3


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
class ArtworkWizart(SessionWizardView):
    form_list = [
        ArtworkForm1,
        ArtworkPaintingForm2, ArtworkBookForm2, ArtworkMovieForm2, ArtworkBookForm3
    ]
    template_name = 'artworks/artwork_wizard_single_unified_template.html'

    def done(self, form_list, form_dict, **kwargs):
        # TODO save data from all of the steps
        print('-------------------done')
        messages.success(self.request,
                         'Artwork successfully saved.')
        return redirect('artworks')
