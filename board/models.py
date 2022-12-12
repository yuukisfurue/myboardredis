from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator  #☆
from django.core.validators import URLValidator  #☆
from django.core.validators import RegexValidator    #☆

class Friend(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(validators=[ \
          MinValueValidator(18), \
          MaxValueValidator(120)])
    jyob =  models.CharField(max_length=100)
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'
import re
from django.db import models
from django.core.validators import ValidationError

def number_only(value):
    if (re.match(r'^[0-9]*$', value) == None):
        raise ValidationError(
            '%(value)s is not Number!', \
            params={'value': value},
        )

class Friend(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    jyob = models.CharField(max_length=200)
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'