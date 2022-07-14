from django.contrib import admin
from .models import QData, SheetCount, KanjiData


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
