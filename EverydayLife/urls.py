from django.urls import path
from .views import choice, rchoice, relative_english, relative_nihongo, relative, shop_english, shop, shop_nihongo, color_english, color_nihongo, color, time_english, time, time_nihongo, wh_english, wh_nihongo, wh

urlpatterns = [

    path('', choice),

    # urls for relative
    path('relative/', rchoice),
    path('relative/english/', relative_english),
    path('relative/nihongo/', relative_nihongo),

    # urls for shop
    path('shop/', rchoice),
    path('shop/english/', shop_english),
    path('shop/nihongo/', shop_nihongo),

    # urls for color
    path('color/', rchoice),
    path('color/english/', color_english),
    path('color/nihongo/', color_nihongo),

    # urls for color
    path('time/', rchoice),
    path('time/english/', time_english),
    path('time/nihongo/', time_nihongo),

    # urls for Wh
    path('wh/', rchoice),
    path('wh/english/', wh_english),
    path('wh/nihongo/', wh_nihongo),

    # get id for relative
    path('relative/<str:get_id>/', relative),
    path('shop/<str:get_id>/', shop),
    path('color/<str:get_id>/', color),
    path('time/<str:get_id>/', time),
    path('wh/<str:get_id>/', wh),

]