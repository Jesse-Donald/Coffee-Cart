from email.errors import CloseBoundaryNotFoundDefect
import uuid
from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(default = uuid.uuid4, editable = False)
    name = models.TextField(primary_key=True)
    drink = models.TextField()
    milk = models.TextField()
    temperature = models.TextField()
    decaf = models.BooleanField()
    strength = models.TextField()
    sugar = models.IntegerField()
    completed = models.BooleanField()
