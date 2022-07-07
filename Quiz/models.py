from django.db import models

class QData(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)