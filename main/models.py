# main/models.py
import uuid
from django.utils import timezone
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.product_views > 20

    def increment_views(self):
        self.product_views += 1
        self.save(update_fields=["product_views"])
