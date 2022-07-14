from django.urls import path
from .views import equiz, choice, nquiz, quiz, kquiz, kdata

urlpatterns = [
    path('', choice),
    path('english/', equiz),
    path('nihongo/', nquiz),
    path('kanji/', kquiz),
    path('<str:get_id>/', quiz),
    path('kanji/<str:get_id>/', kdata),
]