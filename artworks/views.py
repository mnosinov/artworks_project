from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from .insertdatahelper import InserDataHelper
from .models import Genre, Author


def index(request):
    return render(request, 'artworks/index.html')


class InsertSampleDataView(View):
    def get(self, request, *args, **kwargs):
        InserDataHelper(request).reset_data()
        messages.success(request,
                         'Sample Data have been successfully inserted.')
        return redirect('index')


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
