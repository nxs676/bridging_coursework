from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)

    email = models.EmailField()

    summary = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)
    education = models.TextField(max_length=2000)
    jobs = models.TextField(max_length=2000)