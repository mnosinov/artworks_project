from django.urls import path
from .views import index, InsertSampleData

urlpatterns = [
    path('', index, name='index'),
    path('insert-sample-data', InsertSampleData.as_view(), name='insert-sample-data'),
]
