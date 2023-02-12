# Generated by Django 3.0.7 on 2020-06-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_deliveryboy_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryboy',
            name='status',
            field=models.CharField(choices=[['picked', 'picked'], ['on the way', 'on the way'], ['delivered', 'delivered']], default='picked', max_length=30, null=True),
        ),
    ]
