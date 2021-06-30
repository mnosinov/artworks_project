from django.contrib import admin

from .models import Author, Genre, Artwork, Painting, Book, Media


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )
    search_fields = ('name', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artwork_type')
    list_display_links = ('id', 'title', )
    list_filter = ('artwork_type',)
    search_fields = ('title', )


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'genre', 'author', 'pub_year', 'price')
    list_display_links = ('id', 'title', )
    search_fields = ('title', )


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'height', 'width', 'paint')
    list_display_links = ('artwork',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'pages', 'cover')
    list_display_links = ('artwork',)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'media_type', 'duration')
    list_display_links = ('artwork',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Media, MediaAdmin)
