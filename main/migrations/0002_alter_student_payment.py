# Generated by Django 5.2.4 on 2025-07-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='payment',
            field=models.BooleanField(default=True),
        ),
    ]
