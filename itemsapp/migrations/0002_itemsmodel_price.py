# Generated by Django 4.1.5 on 2023-01-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]