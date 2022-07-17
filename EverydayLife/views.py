from django.shortcuts import render
from .models import Relative
import random


def choice(request):

    return render(request, 'dchoice.html')


# choice view for relative
def rchoice(request):

    return render(request, 'rchoice.html')


# view for relative list
def relative_english(request):
    qdata = list(Relative.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'renglish.html', {'i': qdatar})


def relative_nihongo(request):
    qdata = list(Relative.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar})


def relative(request, get_id):
    qdate = Relative.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate})