from django.contrib import admin

from ordering.models import Order
from .models import Order
# Register your models here.
admin.site.register(Order)