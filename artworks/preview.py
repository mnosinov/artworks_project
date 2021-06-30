from django.shortcuts import redirect
from formtools.preview import FormPreview
from django.contrib import messages

from .models import Genre


# formtools - Form Preview -----------------------------------------------
class GenreFormPreview(FormPreview):
    # preview_template = 'artworks/genre_detail.html'
    # form_template = 'artworks/genre_form.html'

    def get_initial(self, request):
        pk = request.GET.get('pk', None)
        if pk:
            genre = Genre.objects.get(pk=pk)
            return genre.__dict__

    def done(self, request, cleaned_data):
        pk = request.GET.get('pk', None)
        genre = Genre(**cleaned_data)
        if pk:
            genre.id = pk
        genre.save()
        messages.success(request,
                         'Genre have been successfully saved.')
        return redirect('genres')
