from django.shortcuts import render
from .models import QData, KanjiData, Question
import random  # added random quarry for all


# 2 choice view

def choice(requset):

    return render(requset, 'choice.html')


def qchoice(requset):

    return render(requset, 'qchoice.html')


# Vocabulary view

def equiz(requset):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'english.html', {'i': qdatar})


def nquiz(requset):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'nihongo.html', {'i': qdatar})


def quiz(requset, get_id):
    qdate = QData.objects.filter(id=get_id).first()
    return render(requset, 'all.html', {'i': qdate})


# Kanji view

def kquiz(requset):
    qdata = list(KanjiData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'kanji.html', {'i': qdatar})


def kdata(requset, get_id):
    qdate = KanjiData.objects.filter(id=get_id).first()
    return render(requset, 'meaning.html', {'i': qdate})


# Question view

def equestion(requset):
    qdata = list(Question.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'qenglish.html', {'i': qdatar})


def nquestion(requset):
    qdata = list(Question.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(requset, 'qnihongo.html', {'i': qdatar})


def question(requset, get_id):
    qdate = Question.objects.filter(id=get_id).first()
    return render(requset, 'question.html', {'i': qdate})