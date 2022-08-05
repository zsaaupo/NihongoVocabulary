from django.db import models


# Relative model
class Relative(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


# Relative model
class Shop(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


# colors model
class Color(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


# Time model
class Time(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


# Wh model
class Wh(models.Model):

    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)

    def __str__(self):
        return self.english


