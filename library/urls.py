from django.urls import path
from .views import BookListView

urlpatterns = [
    path('library/', BookListView.as_view(), name='library'),
]
