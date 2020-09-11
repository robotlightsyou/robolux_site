from django.shortcuts import render
from django.http import HttpResponse
from flashcards.models import Term


# Create your views here.


def home(request):
    context = {
        'terms': Term.objects.all(),
        'title': 'Flashcards-Home',
    }
    return render(request, 'flashcards/home.html', context)


def about(request):
    return HttpResponse('<h1>About flashcards</h1>')
