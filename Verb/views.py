from django.shortcuts import render
from .models import VerbData
import random


def choice(request):

    return render(request, "form_choice.html")

def note(request):

    return render(request, "note.html")


# viwe for forms list
def english_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'english_verb.html', {'i': qdatar})


def basic_form_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'basic_form.html', {'i': qdatar})


def present_positive_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'present_positive.html', {'i': qdatar})


def present_negative_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'present_negative.html', {'i': qdatar})


def past_positive_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'past_positive.html', {'i': qdatar})


def past_negative_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'past_negative.html', {'i': qdatar})


def te_from_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'te_from.html', {'i': qdatar})


def present_continuous_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'present_continuous.html', {'i': qdatar})


def past_continuous_list(request):
    qdata = list(VerbData.objects.all())
    qdatar = random.sample(qdata, len(qdata))
    return render(request, 'past_continuous.html', {'i': qdatar})





# viwe for all form
def all_forms(request, get_id):
    qdate = VerbData.objects.filter(id=get_id).first()
    return render(request, 'all_forms.html', {'i': qdate})
