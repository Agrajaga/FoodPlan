# Generated by Django 4.0.3 on 2022-03-18 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg_food_plan_bot', '0003_customers_ingredients_preferences_recipe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Телефон')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в телеграмме')),
            ],
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='Preferences',
            new_name='Preference',
        ),
        migrations.RenameModel(
            old_name='RecipeIngredients',
            new_name='RecipeIngredient',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_food_plan_bot.customer', verbose_name='Подписка'),
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]