# Generated by Django 3.0.7 on 2020-06-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0002_comment_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]