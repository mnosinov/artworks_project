from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .insertdatahelper import InserDataHelper


def index(request):
    return render(request, 'artworks/index.html')


class InsertSampleData(View):
    def get(self, request, *args, **kwargs):
        InserDataHelper(request).reset_data()
        messages.success(request,
                         'Sample Data have been successfully inserted.')
        return redirect('index')
