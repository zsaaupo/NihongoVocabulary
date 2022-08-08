from django.db import models


# Vocabulary model
class QData(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


class QData2(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


class QData3(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


# Kanji model
class KanjiData(models.Model):

    eigo = models.ForeignKey(QData, on_delete=models.PROTECT, related_name="Nihongo")
    kanji = models.CharField(max_length=100)

    def __str__(self):
        return self.kanji



# Question model
class Question(models.Model):

    english = models.CharField(max_length=10000)
    nihongo = models.CharField(max_length=10000)
    e_positive = models.CharField(max_length=10000, null=True, blank=True)
    n_positive = models.CharField(max_length=10000, null=True, blank=True)
    e_negative = models.CharField(max_length=10000, null=True, blank=True)
    n_negative = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.english


# sheet count model
class SheetCount(models.Model):

    start = models.CharField(max_length=10000)
    end = models.CharField(max_length=10000)

    def __str__(self):
        return self.start