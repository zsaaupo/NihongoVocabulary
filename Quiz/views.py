from django.shortcuts import render
from .models import QData


def choice(requset):

    return render(requset, 'choice.html')


def equiz(requset):
    qdate = QData.objects.filter().all()
    return render(requset, 'english.html', {'i': qdate})

def nquiz(requset):
    qdate = QData.objects.filter().all()
    return render(requset, 'nihongo.html', {'i': qdate})

def quiz(requset, get_id):
    qdate = QData.objects.filter(id=get_id).first()
    return render(requset, 'all.html', {'i': qdate})