from django.shortcuts import render
from django.http import HttpResponse


TESTDECK = {'go': 'execute a cue',
           'stop': 'pause a cue',
           'back': 'restore previous cue',
           'address': 'the digital location of an instrument',
           'query': 'grep patch',
           'snapshot': 'a preset for screen layouts',
           'submaster': 'not a fader',
           'fader': 'a playback for cuelists and other record targets',
           'load': 'prepare a cue in the Go button for next keypress',
           'palette': 'a recorded data object specific to a parameter type',
           'preset': 'a non specific data object, may contain palettes',
           'order 66': 'shutdown macro',
           'macro': 'recorded commands replayed on a single keypress',
           '__dict_name__': 'Sample Deck'}

test2 = [
    {'term': 'go',
     'def': 'execute a cue.'},
    {'term': 'stop',
     'def': 'pause am executing cue.'}
]

# Create your views here.
def home(request):
    context = {
        'test': test2,
        'title': 'Flashcards'
    }
    return render(request, 'flashcards/home.html', context)

def about(request):
    return HttpResponse('<h1>About flashcards</h1>')
