# Generated by Django 3.0.7 on 2020-06-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0003_auto_20200614_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]
