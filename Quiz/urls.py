from django.urls import path
from .views import equiz, choice, nquiz, quiz, kquiz, kdata, qchoice, equestion, nquestion, question

urlpatterns = [
    path('', choice),
    path('english/', equiz),
    path('nihongo/', nquiz),
    path('kanji/', kquiz),
    path('q/', qchoice),
    path('q/english/', equestion),
    path('q/nihongo/', nquestion),
    path('question/<str:get_id>/', question),
    path('<str:get_id>/', quiz),
    path('kanji/<str:get_id>/', kdata),

]