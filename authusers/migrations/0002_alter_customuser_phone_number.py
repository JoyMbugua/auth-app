# Generated by Django 3.2.7 on 2021-09-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=''),
        ),
    ]
