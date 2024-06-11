from django.db import models

# Create your models here.
UL_CHOICES = (
        ('Паспорт гражданина РФ', 'Паспорт гражданина РФ'),
        ('Паспорт иностранного гражданина', 'Паспорт иностранного гражданина'),
    )
EDU_CHOICES = (
        ('Аттестат об основном общем образовании', 'Аттестат об основном общем образовании'),
        ('Аттестат о среднем общем образовании', 'Аттестат о среднем общем образовании'),
        ('Диплом СПО', 'Диплом СПО'),
    )
PARENT_CHOICES = (
        ('Мать', 'Мать'),
        ('Бабушка', 'Бабушка'),
        ('Отец', 'Отец'),
        ('Дедушка', 'Дедушка'),
    )
SOCIAL_CHOICES = (
        ('Отсутствует', 'Отсутствует'),
        ('Ребенок сирота', 'Ребенок сирота'),
        ('Ребенок в тяжелой жизненной ситуации', 'Ребенок в тяжелой жизненной ситуации'),
        ('Ребенок чьи родители находятся на Специальной военной операции',
         'Ребенок чьи родители находятся на Специальной военной операции')
    )
PROGRAM_SELECT = (
        ('СПО', 'СПО'),
        ('Профессия', 'Профессия'),
        ('НПО', 'НПО'),
    )
EDU_SELECT = (
        ('Очная', 'Очная'),
        ('Заочная', 'Заочная'),
    )
FINANCE_SELECT = (
        ('Бюджет', 'Бюджет'),
        ('Вне бюджет', 'Вне бюджет')
    )
COURSE_SELECT = (
        ('1', 'На 1-й курс'),
        ('2', 'На 2-й курс'),
        ('3', 'На 3-й курс'),
        ('4', 'На 4-й курс'),
    )
YN_SELECT = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )


class Specialization(models.Model):
    code = models.CharField(max_length=255)
    spec_name = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    places = models.IntegerField()
    short_name = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.code + ' ' + self.spec_name


class Parent(models.Model):
    id_parent = models.AutoField(primary_key=True)
    parent = models.CharField(max_length=255, choices=PARENT_CHOICES, null=True)
    parent_surname = models.CharField(max_length=255, null=True)
    parent_name = models.CharField(max_length=255, null=True)
    parent_pname = models.CharField(max_length=255, null=True)
    telephone_parent = models.CharField(max_length=255, null=True)
    birthdate = models.DateField(null=True)
    work_place = models.CharField(max_length=255, null=True)


class Identification(models.Model):
    choice = models.CharField(max_length=255, choices=UL_CHOICES, null=True)
    serial_ul = models.CharField(max_length=255, null=True)
    number_ul = models.CharField(max_length=255, null=True)
    gave_out = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    date_out = models.DateField(null=True)


class Education(models.Model):
    eduChoice = models.CharField(max_length=255, choices=EDU_CHOICES, null=True)
    serial_edu = models.CharField(max_length=255, null=True)
    number_edu = models.CharField(max_length=255, null=True)
    edu_out = models.DateField(null=True)
    who_out = models.CharField(max_length=255, null=True)
    year_out = models.DateField(null=True)


class Place(models.Model):
    index = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255, null=True)
    fact_place = models.CharField(max_length=255, null=True)


class IdentityModel(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=255, null=True)
    aname = models.CharField(max_length=255, null=True)
    pname = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    identification_key = models.ForeignKey(Identification, blank=True, null=True, on_delete=models.CASCADE)
    birthplace = models.CharField(max_length=255, null=True)
    insurance = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=255, null=True)
    place_key = models.ForeignKey(Place, blank=True, null=True, on_delete=models.CASCADE)
    edu_key = models.ForeignKey(Education, blank=True, null=True, on_delete=models.CASCADE)
    average_grade = models.CharField(max_length=255, null=True)
    program = models.CharField(max_length=255, choices=PROGRAM_SELECT, null=True)
    form = models.CharField(max_length=255, choices=EDU_SELECT, null=True)
    finance = models.CharField(max_length=255, choices=FINANCE_SELECT, null=True)
    course = models.CharField(max_length=255, choices=COURSE_SELECT, null=True)
    spec = models.ForeignKey(Specialization, blank=True, null=True, on_delete=models.SET_NULL)
    dorm = models.CharField(max_length=3, choices=YN_SELECT, null=True)
    foreign_lan = models.CharField(max_length=255, null=True)
    parent_key = models.ForeignKey(Parent, blank=True, null=True, on_delete=models.CASCADE)
    med = models.CharField(max_length=3, choices=YN_SELECT, null=True)
    photo = models.CharField(max_length=3, choices=YN_SELECT, null=True)
    copy = models.CharField(max_length=3, choices=YN_SELECT, null=True)
    agreement = models.CharField(max_length=3, choices=YN_SELECT, null=True)
    socialStatus = models.CharField(max_length=255, choices=SOCIAL_CHOICES, null=True)
