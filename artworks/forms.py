from django.forms import ModelForm
from .models import Genre


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('title', 'artwork_type')
