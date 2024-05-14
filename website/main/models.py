from django.db import models

# Create your models here.
UL_CHOICES = (
    ('РФ', 'Паспорт гражданина РФ'),
    ('СССР', 'Паспорт гражданина СССР'),
    ('ИНО', 'Паспорт иностранного гражданина'),
)

class TestModel(models.Model):
    choice = models.CharField(max_length=255, choices=UL_CHOICES)