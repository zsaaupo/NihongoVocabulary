from django.contrib import admin
from .models import VerbData


class VerbDataAdmin(admin.ModelAdmin):

    list_display = [

        'english',
        'basic_form'

    ]


admin.site.register(VerbData, VerbDataAdmin)
