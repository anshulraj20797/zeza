from django.db import models


class CustomerMaster(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return self.name