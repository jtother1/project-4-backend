# Generated by Django 3.0.7 on 2020-06-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0010_auto_20200616_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.TextField(default='blank', max_length=300),
        ),
    ]