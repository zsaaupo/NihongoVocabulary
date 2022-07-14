from django.shortcuts import render
from .models import QData, KanjiData
import random


def choice(requset):

    return render(requset, 'choice.html')


# added random quarry for equiz and nquiz

def equiz(requset):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'english.html', {'i': qdatar})


def nquiz(requset):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'nihongo.html', {'i': qdatar})

def kquiz(requset):
    qdata = list(KanjiData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'kanji.html', {'i': qdatar})


def quiz(requset, get_id):
    qdate = QData.objects.filter(id=get_id).first()
    return render(requset, 'all.html', {'i': qdate})


def kdata(requset, get_id):
    qdate = KanjiData.objects.filter(id=get_id).first()
    return render(requset, 'meaning.html', {'i': qdate})