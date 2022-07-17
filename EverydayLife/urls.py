from django.urls import path
from .views import choice, rchoice, relative_english, relative_nihongo, relative

urlpatterns = [

    path('', choice),

    # urls for relative
    path('relative/', rchoice),
    path('relative/english/', relative_english),
    path('relative/nihongo/', relative_nihongo),

    # get id for relative
    path('relative/<str:get_id>/', relative),

]