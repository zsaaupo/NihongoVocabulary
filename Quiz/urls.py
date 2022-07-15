from django.urls import path
from .views import equiz, choice, nquiz, quiz, kquiz, kdata, qchoice, equestion, nquestion, question

urlpatterns = [

    # root url
    path('', choice),

    # Vocabulary Urls
    path('english/', equiz),
    path('nihongo/', nquiz),

    # Kanji Url
    path('kanji/', kquiz),

    # Question Urls
    path('q/', qchoice),
    path('q/english/', equestion),
    path('q/nihongo/', nquestion),

    # all urls with id
    path('<str:get_id>/', quiz),
    path('question/<str:get_id>/', question),
    path('kanji/<str:get_id>/', kdata),

]