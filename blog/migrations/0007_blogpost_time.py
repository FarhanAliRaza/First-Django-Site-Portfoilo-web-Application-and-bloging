# Generated by Django 2.2.7 on 2020-03-25 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200324_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='time',
            field=models.CharField(default='2 min', max_length=10),
        ),
    ]
