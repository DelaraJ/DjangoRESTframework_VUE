from django.db import models
from django.core.validators import MaxValueValidator

class Member(models.Model):
    MALE = 'male'
    FAMALE = 'female'

    STATUS_CHOICES = {
        (MALE, 'Male'),
        (FAMALE, 'Female')
    }

    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)]) #0..10
    age = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    gender = models.CharField(max_length=6, choices=STATUS_CHOICES, default=MALE)