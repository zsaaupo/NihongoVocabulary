from django.shortcuts import render
from .models import QData, KanjiData, Question
import random  # added random quarry for all


# 2 choice view

def choice(request):

    return render(request, 'choice.html')


def qchoice(request):

    return render(request, 'qchoice.html')


# Vocabulary view

def equiz(request):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'english.html', {'i': qdatar})


def nquiz(request):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'nihongo.html', {'i': qdatar})


def quiz(request, get_id):
    qdate = QData.objects.filter(id=get_id).first()
    return render(request, 'all.html', {'i': qdate})


# Kanji view

def kquiz(request):
    qdata = list(KanjiData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'kanji.html', {'i': qdatar})


def kdata(request, get_id):
    qdate = KanjiData.objects.filter(id=get_id).first()
    return render(request, 'meaning.html', {'i': qdate})


# Question view

def equestion(request):
    qdata = list(Question.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'qenglish.html', {'i': qdatar})


def nquestion(request):
    qdata = list(Question.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'qnihongo.html', {'i': qdatar})


def question(request, get_id):
    qdate = Question.objects.filter(id=get_id).first()
    return render(request, 'question.html', {'i': qdate})