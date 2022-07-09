from django.contrib import admin
from .models import QData, SheetCount

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
