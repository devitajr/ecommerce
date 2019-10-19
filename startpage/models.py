from django.db import models

# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=150)

    company_logo_url = models.CharField(max_length=300)

    company_telephone = models.CharField(max_length = 50)

class Category(models.Model):

    name = models.CharField(max_length = 150)

     