from django.db import models

class FieldsToBeSent(models.Model):
    number=models.IntegerField()
    def __str__(self):
        return self.number
