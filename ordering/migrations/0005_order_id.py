# Generated by Django 4.0.5 on 2022-10-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_remove_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
    ]
