from django.urls import path
from .views import student, LendingWive

urlpatterns = [
    path('student/', student, name='student'),
    path('landing/', LendingWive.as_view(), name='lending')
]
