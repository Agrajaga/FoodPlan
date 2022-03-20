from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=25, verbose_name='Имя')
    phone_number = models.CharField(max_length=30, verbose_name="Телефон")
    telegram_id = models.PositiveIntegerField(
        verbose_name="ID пользователя в телеграмме", unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.username


class Preference(models.Model):
    type = models.CharField(max_length=30, verbose_name="Предпочтение")

    class Meta:
        verbose_name = "Предпочтение"
        verbose_name_plural = "Предпочтения"

    def __str__(self):
        return self.type


class Subscription(models.Model):
    owner = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Подписка")
    register_date = models.DateField()
    paid_until = models.DateField()
    person_amount = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name="Количество персон")
    preferences = models.ForeignKey(
        Preference, on_delete=models.CASCADE, verbose_name="Предпочтение")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.owner} - {self.person_amount}'

class Ingredient(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название ингредиента")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название блюда")
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    preferences = models.ManyToManyField(
        Preference,
        through="RecipeClassificator",
        through_fields=("recipe", "preferences"),
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        through_fields=("recipe", "ingredient"),
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class RecipeClassificator(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    preferences = models.ForeignKey(Preference, on_delete=models.CASCADE)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_amount = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name="Количество ингредиента")
    ingredient_measure = models.CharField(
        max_length=30, verbose_name="Единица измерения")
