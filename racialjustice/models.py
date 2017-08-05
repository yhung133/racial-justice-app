from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Arrest(models.Model):
    arrestee_id = models.IntegerField()
    arrest_date = models.DateField()
    arrest_time = models.TimeField()
    arrest_code = models.TextField()
    arrest_location = models.TextField()
    crime_code = models.TextField()
    crime_code_description = models.TextField()
    crime_code_category = models.TextField()
    crime_code_category_description = models.TextField()
    weapon_code_1 = models.CharField(max_length=30)
    weapon_code_2 = models.CharField(max_length=30)
    weapon_code_3 = models.CharField(max_length=30)
    race = models.TextField()
    sex = models.TextField()
    age = models.IntegerField()
    employment_code = models.CharField(max_length=30)
    arrest_officer_code = models.IntegerField()
    result = models.TextField()
    jurisdiction = models.TextField()
    more_than_one_charge = models.IntegerField()
    mvo = models.IntegerField()
    