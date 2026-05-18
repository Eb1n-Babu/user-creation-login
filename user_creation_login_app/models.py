from django.db import models

class Accounts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'