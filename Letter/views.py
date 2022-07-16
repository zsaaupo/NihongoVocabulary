from django.shortcuts import render
from .models import Hiragana, Katakana
import random  # added random quarry for all


# choice viwe

def lchoice(request):

    return render(request, "lchoice.html")


def hiragana(requset):
    qdata = list(Hiragana.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'hiragana.html', {'i': qdatar})


def katakana(requset):
    qdata = list(Katakana.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'katakana.html', {'i': qdatar})


def hiragana_pronounce(requset, get_id):
    qdate = Hiragana.objects.filter(id=get_id).first()
    return render(requset, 'hiraganap.html', {'i': qdate})


def katakana_pronounce(requset, get_id):
    qdate = Katakana.objects.filter(id=get_id).first()
    return render(requset, 'katakanap.html', {'i': qdate})