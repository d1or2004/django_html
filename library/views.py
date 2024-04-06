from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'library.html', context)
