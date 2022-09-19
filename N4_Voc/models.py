from django.db import models

# list 1

class N4L(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english

class KanjiN4(models.Model):

    eigo = models.ForeignKey(N4L, on_delete=models.PROTECT, related_name="Nihongo")
    kanji = models.CharField(max_length=100)

    def __str__(self):
        return self.kanji