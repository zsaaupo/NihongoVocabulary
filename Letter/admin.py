from django.contrib import admin
from .models import Hiragana, Katakana


# ひらがな admin
class HiraganaAdmin(admin.ModelAdmin):

    fields = [
        "hiragana",
        "pronounce"
    ]
    list_display = [
        "hiragana",
        "pronounce"
    ]


admin.site.register(Hiragana, HiraganaAdmin)


# カタカナ admin
class KatakanaAdmin(admin.ModelAdmin):
    fields = [
        "katakana",
        "pronunciation"
    ]
    list_display = [
        "katakana",
        "pronunciation"
    ]


admin.site.register(Katakana, KatakanaAdmin)

