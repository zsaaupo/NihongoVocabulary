from django.db import models

class QData(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english

class KanjiData(models.Model):

    eigo = models.ForeignKey(QData, on_delete=models.PROTECT, related_name="Nihongo")
    kanji = models.CharField(max_length=100)

    def __str__(self):
        return self.kanji


class SheetCount(models.Model):

    start = models.CharField(max_length=10000)
    end = models.CharField(max_length=10000)

    def __str__(self):
        return self.start