from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('letter/', include("Letter.urls")),
    path('everydaylife/', include("EverydayLife.urls")),
    path('', include("Quiz.urls")),
]
