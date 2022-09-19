from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('letter/', include("Letter.urls")),
    path('everydaylife/', include("EverydayLife.urls")),
    path('verb/', include("Verb.urls")),
    path('', include("Quiz.urls")),
    path('N4/', include("N4_Voc.urls")),
]
