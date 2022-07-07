from django.urls import path
from .views import equiz, choice, nquiz, quiz

urlpatterns = [
    path('', choice),
    path('english/', equiz),
    path('nihongo/', nquiz),
    path('<str:get_id>/', quiz),
]