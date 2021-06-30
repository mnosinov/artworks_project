from django.urls import path
from .views import index, InsertSampleDataView, GenreListView, GenreDetailView, \
        GenreUpdateView, GenreDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('insert-sample-data', InsertSampleDataView.as_view(), name='insert-sample-data'),
    path('genres', GenreListView.as_view(), name='genres'),
    path('genres/<int:pk>/view', GenreDetailView.as_view(), name='genre-detail-view'),
    path('genres/<int:pk>/update', GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete', GenreDeleteView.as_view(), name='genre-delete'),
]
