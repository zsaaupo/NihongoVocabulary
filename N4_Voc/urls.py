from django.urls import path
from .views import voc_choice, language_choice, equiz, nquiz, quiz, kdata, kquiz


urlpatterns = [

    # N4 list choice
    path('', voc_choice),

    # language choice
    path('1/', language_choice),

    # Vocabulary Urls
    path('1/english/', equiz),
    path('1/nihongo/', nquiz),

    # Kanji Url
    path('kanji/', kquiz),

    # all urls with id
    path('1/<str:get_id>/', quiz),
    path('kanji/<str:get_id>/', kdata),
]