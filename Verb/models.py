from django.db import models


# model for verb's forms
class VerbData(models.Model):

    basic_form = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    present_positive = models.CharField(max_length=50)
    present_negative = models.CharField(max_length=50)
    past_positive = models.CharField(max_length=50)
    past_negative = models.CharField(max_length=50)
    te_from = models.CharField(max_length=50)
    present_continuous = models.CharField(max_length=50)
    past_continuous = models.CharField(max_length=50)

    def __str__(self):
        return self.basic_form