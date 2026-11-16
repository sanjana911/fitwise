from django.db import models

# Create your models here.

#foodlog(title,calorie, mealtype,serving_size, created_at,owner)

class Foodlog(models.Model):

    title = models.CharField(max_length=200)

    calorie = models.FloatField()

    MEAL_TYPE_OPTIONS = (
        ("BREAKFAST","breakfast"),
        ("LUNCH","lunch"),
        ("SNACKS","snacks"),
        ("DINNER","dinner")
    )

    meal_type = models.CharField(max_length=100, choices= MEAL_TYPE_OPTIONS, default="BREAKFAST")

    serving_size = models.CharField(max_length=100)

    created_at = models.DateField()

    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.title