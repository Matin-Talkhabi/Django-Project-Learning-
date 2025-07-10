from django.db import models


# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=25)
    address = models.CharField(max_length=140)
    img = models.ImageField(upload_to='project', null=False)

    def __str__(self):
        return self.title + self.description


class ticket(models.Model):
    name = models.CharField(max_length=20 , null=False)
    email = models.CharField(max_length=25 , null=False)
    title = models.CharField(max_length=20 , null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name + self.title


class footer(models.Model):
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=25 , null=False)

    instagram = models.CharField(max_length=25 , null=False)
    telegram = models.CharField(max_length=25 , null=False)
    whatsapp = models.CharField(max_length=25 , null=False)
