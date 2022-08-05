from django.contrib import admin
from .models import Relative, Shop, Color


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
