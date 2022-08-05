from django.shortcuts import render
from .models import Relative, Shop, Color, Time, Wh
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
    return render(request, 'renglish.html', {'i': qdatar, 'r': 'relative'})


def relative_nihongo(request):
    qdata = list(Relative.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar, 'r': 'relative'})


def relative(request, get_id):
    qdate = Relative.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate, 'r': 'relative'})


# view for shop list
def shop_english(request):
    qdata = list(Shop.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'renglish.html', {'i': qdatar, 'r': 'shop'})


def shop_nihongo(request):
    qdata = list(Shop.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar, 'r': 'shop'})


def shop(request, get_id):
    qdate = Shop.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate, 'r': 'shop'})


# view for Colors
def color_english(request):
    qdata = list(Color.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'renglish.html', {'i': qdatar, 'r': 'color'})


def color_nihongo(request):
    qdata = list(Color.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar, 'r': 'color'})


def color(request, get_id):
    qdate = Color.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate, 'r': 'color'})


# view for Time
def time_english(request):
    qdata = list(Time.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'renglish.html', {'i': qdatar, 'r': 'time'})


def time_nihongo(request):
    qdata = list(Time.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar, 'r': 'time'})


def time(request, get_id):
    qdate = Time.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate, 'r': 'time'})


# view for Wh
def wh_english(request):
    qdata = list(Wh.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'renglish.html', {'i': qdatar, 'r': 'wh'})


def wh_nihongo(request):
    qdata = list(Wh.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'rnihongo.html', {'i': qdatar, 'r': 'wh'})


def wh(request, get_id):
    qdate = Wh.objects.filter(id=get_id).first()
    return render(request, 'relative.html', {'i': qdate, 'r': 'wh'})