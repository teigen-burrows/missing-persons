from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    personFirstName = models.CharField(max_length=100)
    personLastName = models.CharField(max_length=100)
    personAgeMissing = models.IntegerField(null=False)
    personDateMissing = models.DateField()
    personCity = models.CharField(max_length=50)
    personState = models.CharField(max_length=2)
    personGender = models.CharField(max_length=1)
    personRace = models.CharField(max_length=1)
    @property
    def personFullName(self):
        return '%s %s' %(self.personFirstName, self.personLastName)
