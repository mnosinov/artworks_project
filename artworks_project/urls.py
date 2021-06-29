from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('artworks.urls')),
    path('admin/', admin.site.urls),
]
