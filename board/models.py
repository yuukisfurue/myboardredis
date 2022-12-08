from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    jyob = models.CharField(max_length=100)
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'