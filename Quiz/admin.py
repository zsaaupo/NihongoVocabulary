from django.contrib import admin
from .models import QData

class QDataAdmin(admin.ModelAdmin):
    fields = [
        "english",
        "nihongo"
    ]
    list_display = [
        "english",
        "nihongo"
    ]
admin.site.register(QData,QDataAdmin)

