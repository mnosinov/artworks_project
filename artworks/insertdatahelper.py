from django.contrib import messages
from .models import Author


class InserDataHelper():
    def __init__(self, request):
        self.request = request

    def reset_data(self):
        insert_authors()
        cnt = Author.objects.count()
        messages.success(self.request, 'authors inserted ' + str(cnt))


def insert_authors():
    Author.objects.create(name='Arthur')
    Author.objects.create(name='John')
    Author.objects.create(name='Ann')
    Author.objects.create(name='Dave')
    Author.objects.create(name='Robert')
