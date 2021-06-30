from django.contrib import admin

from .models import Author, Genre


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artwork_type')
    list_display_links = ('id', 'title', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
