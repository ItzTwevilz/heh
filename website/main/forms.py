from django import forms
from django.forms import ModelForm
from .models import *


class TestForm(ModelForm):
    class Meta:
        model = IdentityModel
        fields = '__all__'
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'pname': 'Отчество',
            'birthday': 'День рождения',
            'birthplace': 'Место рождения',
            'insurance': 'СНИЛС',
            'telephone': 'Телефон',
            'average_grade': 'Средний балл',
            'program': 'Программа подготовки',
            'form': 'Форма обучения',
            'finance': 'Финансирование',
            'course': 'Курс',
            'spec': 'Специальность',
            'dorm': 'Нуждается в общежитии',
            'foreign_lan': 'Иностранный язык',
            'med': 'Медицинская справка',
            'photo': '4 фото 3x4',
            'copy': 'Копия СНИЛС',
            'agreement': 'Согласие на обработку ПДн',
            'socialStatus': 'Социальный статус',
        }
        widgets = {
            'program': forms.RadioSelect(),
            'form': forms.RadioSelect(),
            'finance': forms.RadioSelect(),
            'course': forms.RadioSelect(),
            'dorm': forms.RadioSelect(),
            'med': forms.RadioSelect(),
            'photo': forms.RadioSelect(),
            'copy': forms.RadioSelect(),
            'agreement': forms.RadioSelect(),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': "date",
            }),
            'spec': forms.Select()
        }


class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
        labels = {
            'parent': 'Родитель/опекун',
            'parent_surname': 'Фамилия',
            'parent_name': 'Имя',
            'parent_pname': 'Отчество',
            'telephone_parent': 'Телефон',
            'birthdate': 'Дата рождения',
            'workplace': 'Место работы',
        }
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': "date",
            }),
        }


class PassportForm(ModelForm):
    class Meta:
        model = Identification
        fields = '__all__'
        labels = {
            'choice': 'Тип паспорта',
            'serial_ul': 'Серия паспорта',
            'number_ul': 'Номер паспорта',
            'gave_out': 'Кем выдан',
            'code': 'Код подразделения',
            'date_out': 'Когда выдан',
        }
        widgets = {
            'date_out': forms.DateInput(attrs={
                'class': 'form-control',
                'type': "date",
            }),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        labels = {
            'eduChoice': 'Тип образования',
            'serial_edu': 'Серия образования',
            'number_edu': 'Номер образования',
            'edu_out': 'Когда выдано',
            'who_out': 'Кем выдано',
            'year_out': 'Год окончания',
        }
        widgets = {
            'edu_out': forms.DateInput(attrs={
                'class': 'form-control',
                'type': "date",
            }),
            'year_out': forms.DateInput(attrs={
                'class': 'form-control',
                'type': "date",
            }),
        }


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        labels = {
            'index': 'Индекс',
            'region': 'Регион',
            'district': 'Район',
            'town': 'Населенный пункт',
            'place': 'Улица, дом, кв.',
            'fact_place': 'Фактическое место жительства',
        }
