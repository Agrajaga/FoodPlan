# Generated by Django 4.0.3 on 2022-03-17 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tg_food_plan_bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]