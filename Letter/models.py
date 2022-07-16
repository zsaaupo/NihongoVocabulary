from django.db import models


# model for ひらがな
class Hiragana(models.Model):

    hiragana = models.CharField(max_length=20)
    pronounce = models.CharField(max_length=20)

    def __str__(self):
        return self.pronounce


# model for カタカナ
class Katakana(models.Model):

    pronunciation = models.ForeignKey(Hiragana, on_delete=models.PROTECT, related_name="Pronounce")
    katakana = models.CharField(max_length=20)

    def __str__(self):
        return self.katakana