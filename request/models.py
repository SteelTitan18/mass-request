from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import *
from django.contrib.postgres.fields import ArrayField


class NewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=ChurchRequest.Status.NEW)


class Church(models.Model):
    name = models.fields.CharField(verbose_name="Nom ", max_length=100)
    secretary = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_church')
    status = models.fields.CharField(verbose_name="Status", max_length=30, choices=[('top', 'Paroisse'),
                                                                                    ('second', 'Station secondaire')])
    archdiocese = models.fields.CharField(verbose_name="Archidiocèse ", max_length=30)
    priest = models.fields.CharField(verbose_name="Curé ", max_length=100)
    mother_parish = models.fields.CharField(verbose_name="Paroisse mère ", max_length=100, blank=True, null=True)
    tmoney_number = PhoneNumberField(verbose_name="Numéro Tmoney", unique=True)
    flooz_number = PhoneNumberField(verbose_name="Numéro Flooz", unique=True)


class ChurchRequest(models.Model):
    class Status(models.TextChoices):
        NEW = 'NW', 'New'
        REPORTED = 'RP', 'Reported'

    class Hours(models.TextChoices):
        DAWN = 'DN', '6h'
        MORNING = 'MN', '9h'
        MIDDAY = 'MD', '12h'
        EVENING = 'EV', '17h'

    customer = models.fields.CharField(verbose_name="Demandée par ", max_length=30)
    content = models.fields.TextField(verbose_name="Intention (Veuillez être clair, précis et bref)\n", max_length=200)
    dates = ArrayField(models.DateField())
    hours = models.fields.CharField(verbose_name="Horaires ", choices=Hours.choices, max_length=3)
    request_church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="request_church")
    status = models.fields.CharField(max_length=2, choices=Status.choices, default=Status.NEW)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # default manager
    news = NewsManager()  # customer manager

    # default  order of rendering
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-status'])
        ]

    def __str__(self):
        return f'{self.id}'


class Suggestion(models.Model):
    content = models.fields.CharField(verbose_name="Contenu ", max_length=200)
    suggestion_church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="suggestion_church")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # default  order of rendering
    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.content


class Announcement(models.Model):
    title = models.fields.CharField(verbose_name="Titre ", max_length=50)
    content = models.fields.CharField(verbose_name="Contenu ", max_length=200)
    illustration = models.ImageField(default=None, blank=True, null=True, upload_to='images/illustrations/%Y/%m/%d/')
    announcement_church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="announcement_church")

    def __str__(self):
        return self.title
