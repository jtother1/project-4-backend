# Generated by Django 3.0.7 on 2020-06-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0009_auto_20200616_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=300),
        ),
    ]
