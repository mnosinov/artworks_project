from django import forms

from .models import Genre, ArtworkType, Author


# used for formtools - FormPreview sample
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('title', 'artwork_type')


# wizard forms - for Artwork ----------------------------
# step1
class ArtworkForm1(forms.Form):
    title = forms.CharField(max_length=200)
    type = forms.ChoiceField(choices=ArtworkType.choices)
    author = forms.ModelChoiceField(queryset=Author.objects)
    pub_year = forms.IntegerField()


# step2
class ArtworkPaintingForm2(forms.Form):
    # genre can be unknown - null
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.filter(artwork_type=ArtworkType.PAINTING)
    )


class ArtworkMusicForm2(forms.Form):
    # genre can be unknown - null
    genre = forms.ModelChoiceField(queryset=Genre.objects)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.filter(artwork_type=ArtworkType.MUSIC)
    )


class ArtworkMovieForm2(forms.Form):
    # genre can be unknown - null
    genre = forms.ModelChoiceField(queryset=Genre.objects)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.filter(artwork_type=ArtworkType.MOVIE)
    )


class ArtworkBookForm2(forms.Form):
    # genre can be unknown - null
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.filter(artwork_type=ArtworkType.BOOK)
    )


# step3
class ArtworkPaintingForm3(forms.Form):
    height = forms.IntegerField()
    width = forms.IntegerField()


class ArtworkMusicForm3(forms.Form):
    duration = forms.DurationField()


class ArtworkMovieForm3(forms.Form):
    duration = forms.DurationField()


class ArtworkBookForm3(forms.Form):
    pages = forms.IntegerField()


# step4
class ArtworkPaintingForm4(forms.Form):
    paint = forms.CharField(max_length=30)


class ArtworkMusicForm4(forms.Form):
    price = forms.IntegerField()


class ArtworkMovieForm4(forms.Form):
    price = forms.IntegerField()


class ArtworkBookForm4(forms.Form):
    cover = forms.ImageField()


# step5
class ArtworkPaintingForm5(forms.Form):
    price = forms.IntegerField()


class ArtworkBookForm5(forms.Form):
    price = forms.IntegerField()


# confirmation
class ArtworkConfirmationForm(forms.Form):
    pass
