from django.db import models

class persons(models.Model):

    name =  models.CharField(max_length=100)
    pregnancies = models.IntegerField(default=0)
    glucose = models.IntegerField(default=0)
    bp = models.IntegerField(default=0)
    skin = models.IntegerField(default=0)
    insulin = models.IntegerField(default=0)
    bmi = models.IntegerField(default=0)
    Diabetes = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)