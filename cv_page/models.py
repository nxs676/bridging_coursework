from django.core.exceptions import ValidationError
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

    def __str__(self):
        return self.name

    def clean(self):
        if not self.pk and CV.objects.exists():
            raise ValidationError('There can only be one CV instance')

    def save(self, *args, **kwargs):
        return super(CV, self).save(*args, **kwargs)