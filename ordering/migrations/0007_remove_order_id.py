# Generated by Django 4.0.5 on 2022-10-10 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0006_alter_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
    ]