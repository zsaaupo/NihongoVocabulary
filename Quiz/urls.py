from django.urls import path
from .views import equiz, choice, nquiz, quiz, kquiz, kdata, qchoice, equestion, nquestion, question, quiz2, equiz2, nquiz2, voc_choice, language_choice1, language_choice2, language_choice3, nquiz3, equiz3, quiz3

urlpatterns = [

    # root url
    path('', choice),

    # Vocabulary choice list
    path('list/', voc_choice),
    path('list/1/', language_choice1),
    path('list/2/', language_choice2),
    path('list/3/', language_choice3),

    # Vocabulary Urls
    path('list/1/english/', equiz),
    path('list/1/nihongo/', nquiz),
    path('list/2/english/', equiz2),
    path('list/2/nihongo/', nquiz2),
    path('list/3/english/', equiz3),
    path('list/3/nihongo/', nquiz3),

    # Kanji Url
    path('kanji/', kquiz),

    # Question Urls
    path('q/', qchoice),
    path('q/english/', equestion),
    path('q/nihongo/', nquestion),

    # all urls with id
    path('1/<str:get_id>/', quiz),
    path('2/<str:get_id>/', quiz2),
    path('3/<str:get_id>/', quiz3),
    path('question/<str:get_id>/', question),
    path('kanji/<str:get_id>/', kdata),

]