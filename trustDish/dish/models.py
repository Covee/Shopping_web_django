from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    portion = models.IntegerField()
    thumbnail = models.ImageField()
    image = models.ImageField()
    description = models.TextField()
    

    def __str__(self):
        return self.name
    

class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField()
    star = models.FloatField()

    def __str__(self):
        return self.title


class DishQA(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return self.title 