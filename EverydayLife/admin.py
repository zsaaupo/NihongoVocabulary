from django.contrib import admin
from .models import Relative


class RelativeAdmin(admin.ModelAdmin):

    fields = [
        'english',
        'nihongo'
    ]

    list_display = [
        'english',
        'nihongo'
    ]

admin.site.register(Relative, RelativeAdmin)