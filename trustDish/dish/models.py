from django.db import models


class Dish(models.Model):
    name = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

# class 