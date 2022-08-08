from django.contrib import admin
from .models import QData, SheetCount, KanjiData, Question, QData2, QData3


# Vocabulary admin
class QDataAdmin(admin.ModelAdmin):
    fields = [
        "english",
        "nihongo"
    ]
    list_display = [
        "english",
        "nihongo"
    ]


admin.site.register(QData, QDataAdmin)


class QData2Admin(admin.ModelAdmin):
    fields = [
        "english",
        "nihongo"
    ]
    list_display = [
        "english",
        "nihongo"
    ]


admin.site.register(QData2, QData2Admin)


class QData3Admin(admin.ModelAdmin):
    fields = [
        "english",
        "nihongo"
    ]
    list_display = [
        "english",
        "nihongo"
    ]


admin.site.register(QData3, QData3Admin)

# Kanji admin
class KanjiDataAdmin(admin.ModelAdmin):

    fields = [
        "eigo",
        "kanji"
    ]
    list_display = [
        "kanji",
        "eigo"

    ]


admin.site.register(KanjiData, KanjiDataAdmin)


# Question admin
class QuestionAdmin(admin.ModelAdmin):

    fields = [
        "english",
        "nihongo",
        "e_positive",
        "n_positive",
        "e_negative",
        "n_negative"
    ]
    list_display = [
        "english",
        "nihongo"
    ]


admin.site.register(Question, QuestionAdmin)


# count for listing
class SheetCountAdmin(admin.ModelAdmin):
    fields = [
        "start",
        "end"
    ]

    list_display = [
        "start",
        "end"
    ]


admin.site.register(SheetCount, SheetCountAdmin)
