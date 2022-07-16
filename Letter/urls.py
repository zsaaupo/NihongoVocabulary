from django.contrib import admin
from django.urls import path
from .views import lchoice, hiragana, katakana, hiragana_pronounce, katakana_pronounce


urlpatterns = [
    path('', lchoice),
    path('hiragana/', hiragana),
    path('katakana/', katakana),
    path('hiragana/<str:get_id>/', hiragana_pronounce),
    path('katakana/<str:get_id>/', katakana_pronounce),
]