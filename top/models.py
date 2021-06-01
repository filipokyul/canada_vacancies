from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=20)

class Cities(models.Model):
    name = models.CharField(max_length=20)

class CityLangVac(models.Model):
    id_lang = models.IntegerField()
    id_city = models.IntegerField()
    vacancies_number = models.IntegerField()
