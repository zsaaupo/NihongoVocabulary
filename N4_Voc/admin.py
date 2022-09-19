from django.contrib import admin
from .models import N4L, KanjiN4


# Vocabulary admin
class N4LAdmin(admin.ModelAdmin):
    fields = [
        "english",
        "nihongo"
    ]
    list_display = [
        "english",
        "nihongo"
    ]


admin.site.register(N4L, N4LAdmin)


# Kanji admin
class KanjiN4Admin(admin.ModelAdmin):

    fields = [
        "eigo",
        "kanji"
    ]
    list_display = [
        "kanji",
        "eigo"

    ]


admin.site.register(KanjiN4, KanjiN4Admin)