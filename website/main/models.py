from django.db import models

# Create your models here.
EDU_CHOICES = (
    ('1', 'Аттестат об основном общем образовании'),
    ('2', 'Аттестат о среднем общем образовании'),
    ('3', 'Диплом СПО'),
)

class IdentityModel(models.Model):
    UL_CHOICES = (
        ('РФ', 'Паспорт гражданина РФ'),
        ('ИНО', 'Паспорт иностранного гражданина'),
    )
    EDU_CHOICES = (
        (1, 'Аттестат об основном общем образовании'),
        (2, 'Аттестат о среднем общем образовании'),
        (3, 'Диплом СПО'),
    )
    FPARENT_CHOICES = (
        ('Мать', 'Мать'),
        ('Бабушка', 'Бабушка'),
    )
    MPARENT_CHOICES = (
        ('Отец', 'Отец'),
        ('Дедушка', 'Дедушка')
    )
    SOCIAL_CHOICES = (
        ('Сирота', 'Ребенок сирота'),
        ('ТЖС', 'Ребенок в тяжелой жизненной ситуации'),
        ('СВО', 'Ребенок чьи родители находятся на Специальной военной операции')
    )
    choice = models.CharField(max_length=255, choices=UL_CHOICES)
    eduChoice = models.CharField(max_length=255, choices=EDU_CHOICES)
    fparent = models.CharField(max_length=255, choices=FPARENT_CHOICES)
    mparent = models.CharField(max_length=255, choices=MPARENT_CHOICES)
    socialStatus = models.CharField(max_length=255, choices=SOCIAL_CHOICES)