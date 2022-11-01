from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    team = models.CharField(max_length=40)
    number = models.IntegerField()
    position = models.CharField(max_length=40)

    def  __str__(self):
        return f"{self.name} - {self.last_name} - {self.number}"