from django.shortcuts import render
from .models import QData, KanjiData, Question, QData2, QData3
import random  # added random quarry for all


# 2 choice view

def choice(request):

    return render(request, 'choice.html')


def qchoice(request):

    return render(request, 'qchoice.html')


def voc_choice(request):

    return render(request, 'voc_choice.html')


def language_choice1(request):

    return render(request, 'language_choice.html', {"no": "1"})


def language_choice2(request):

    return render(request, 'language_choice.html', {"no": "2"})


def language_choice3(request):

    return render(request, 'language_choice.html', {"no": "3"})


# Vocabulary view

# Voc list 1
def equiz(request):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "1"
    return render(request, 'english.html', {'i': qdatar, 'page': page_no})


def nquiz(request):
    qdata = list(QData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "1"
    return render(request, 'nihongo.html', {'i': qdatar, 'page': page_no})


def quiz(request, get_id):
    qdate = QData.objects.filter(id=get_id).first()
    page_no = "1"
    return render(request, 'all.html', {'i': qdate, 'page': page_no})


# Voc list 2
def equiz2(request):
    qdata = list(QData2.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "2"
    return render(request, 'english.html', {'i': qdatar, 'page': page_no})


def nquiz2(request):
    qdata = list(QData2.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "2"
    return render(request, 'nihongo.html', {'i': qdatar, 'page': page_no})


def quiz2(request, get_id):
    qdate = QData2.objects.filter(id=get_id).first()
    page_no = "2"
    return render(request, 'all.html', {'i': qdate, 'page': page_no})


# Voc list 3
def equiz3(request):
    qdata = list(QData3.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "3"
    return render(request, 'english.html', {'i': qdatar, 'page': page_no})


def nquiz3(request):
    qdata = list(QData3.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    page_no = "3"
    return render(request, 'nihongo.html', {'i': qdatar, 'page': page_no})


def quiz3(request, get_id):
    qdate = QData3.objects.filter(id=get_id).first()
    page_no = "3"
    return render(request, 'all.html', {'i': qdate, 'page' : page_no})


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