from django import template
from artworks.models import Artwork, Book, Painting, Media, ArtworkType

register = template.Library()


@register.inclusion_tag('artworks/inc/artwork_details_by_type.html')
def artwork_details(artwork_id, is_short_mode, **kwargs):
    artwork = Artwork.objects.get(pk=artwork_id)
    if artwork.type == ArtworkType.PAINTING:
        detail = Painting.objects.get(pk=artwork.id)
    elif artwork.type == ArtworkType.MUSIC:
        detail = Media.objects.get(pk=artwork.id)
    elif artwork.type == ArtworkType.MOVIE:
        detail = Media.objects.get(pk=artwork.id)
    elif artwork.type == ArtworkType.BOOK:
        detail = Book.objects.get(pk=artwork.id)
    return {'object': artwork, 'detail': detail, 'is_short_mode': is_short_mode}
