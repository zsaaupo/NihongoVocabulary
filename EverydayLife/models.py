from django.db import models

# Relative model
class Relative(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english