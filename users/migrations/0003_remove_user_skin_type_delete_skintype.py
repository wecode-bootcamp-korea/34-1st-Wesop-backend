# Generated by Django 4.0.5 on 2022-06-27 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_review_reviewimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='skin_type',
        ),
        migrations.DeleteModel(
            name='Skintype',
        ),
    ]
