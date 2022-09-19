from django.shortcuts import render
from .models import N4L, KanjiN4
import random  # added random quarry for all


# list choice
def voc_choice(request):

    return render(request, 'voc_choice.html')


# language choice
def language_choice(request):

    return render(request, 'language_choice.html')


# Voc list N4 1

def equiz(request):
    qdata = list(N4L.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "1"
    return render(request, 'english_N4.html', {'i': qdatar, 'page': page_no})


def nquiz(request):
    qdata = list(N4L.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "1"
    return render(request, 'nihongo_N4.html', {'i': qdatar, 'page': page_no})


def quiz(request, get_id):
    qdate = N4L.objects.filter(id=get_id).first()
    page_no = "1"
    return render(request, 'all_N4.html', {'i': qdate, 'page': page_no})


# Kanji view
def kquiz(request):
    qdata = list(KanjiN4.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'kanji_N4.html', {'i': qdatar})


def kdata(request, get_id):
    qdate = KanjiN4.objects.filter(id=get_id).first()
    return render(request, 'meaning.html', {'i': qdate})