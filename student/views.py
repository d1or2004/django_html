from django.shortcuts import render
from django.views import View


def student(request):
    return render(request, 'student.html')


class LendingWive(View):
    def get(self, request):
        return render(request, 'landing.html')
