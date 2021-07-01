from django.urls import path
from .views import index, InsertSampleDataView, \
    GenreListView, GenreDetailView, GenreUpdateView, GenreDeleteView, GenreCreateView, \
    AuthorListView, AuthorDetailView, AuthorUpdateView, AuthorDeleteView, AuthorCreateView, \
    ArtworkListView, ArtworkDetailView, ArtworkUpdateView, ArtworkDeleteView, \
    ArtworkWizart
from .preview import GenreFormPreview
from .forms import GenreForm

urlpatterns = [
    path('', index, name='index'),
    path('insert-sample-data', InsertSampleDataView.as_view(), name='insert-sample-data'),
    path('genres', GenreListView.as_view(), name='genres'),
    path('genres/create', GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/view', GenreDetailView.as_view(), name='genre-detail-view'),
    path('genres/<int:pk>/update', GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete', GenreDeleteView.as_view(), name='genre-delete'),
    path('authors', AuthorListView.as_view(), name='authors'),
    path('authors/create', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/view', AuthorDetailView.as_view(), name='author-detail-view'),
    path('authors/<int:pk>/update', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete', AuthorDeleteView.as_view(), name='author-delete'),
    path('artworks', ArtworkListView.as_view(), name='artworks'),
    path('artworks/<int:pk>/view', ArtworkDetailView.as_view(), name='artwork-detail-view'),
    path('artworks/<int:pk>/update', ArtworkUpdateView.as_view(), name='artwork-update'),
    path('artworks/<int:pk>/delete', ArtworkDeleteView.as_view(), name='artwork-delete'),
    # formtools FormPreview
    path('genres/formtools-preview', GenreFormPreview(GenreForm), name='genre-formtools-preview'),
    # formtools Artwork wizard
    path('artworks/create', ArtworkWizart.as_view(), name='artwork-create-wizard'),
]
