# Generated by Django 2.2.7 on 2020-03-25 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='imp',
            field=models.CharField(default='ok', max_length=40),
        ),
    ]
