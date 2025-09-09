from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name
