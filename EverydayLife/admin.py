from django.contrib import admin
from .models import Relative, Shop, Color, Time, Wh


# relative admin
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


# shop admin
class ShopAdmin(admin.ModelAdmin):

    fields = [
        'english',
        'nihongo'
    ]

    list_display = [
        'english',
        'nihongo'
    ]


admin.site.register(Shop, ShopAdmin)


# Colors admin
class ColorAdmin(admin.ModelAdmin):

    fields = [
        'english',
        'nihongo'
    ]

    list_display = [
        'english',
        'nihongo'
    ]


admin.site.register(Color, ColorAdmin)


# Time admin
class TimeAdmin(admin.ModelAdmin):

    fields = [
        'english',
        'nihongo'
    ]

    list_display = [
        'english',
        'nihongo'
    ]


admin.site.register(Time, TimeAdmin)


# Wh admin
class WhAdmin(admin.ModelAdmin):

    fields = [
        'english',
        'nihongo'
    ]

    list_display = [
        'english',
        'nihongo'
    ]


admin.site.register(Wh, WhAdmin)
