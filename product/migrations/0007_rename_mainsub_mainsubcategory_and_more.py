# Generated by Django 4.0.5 on 2022-06-23 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_is_show_all'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mainsub',
            new_name='Mainsubcategory',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_show_all',
        ),
    ]