# Generated by Django 4.0.5 on 2022-10-10 09:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0007_remove_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]