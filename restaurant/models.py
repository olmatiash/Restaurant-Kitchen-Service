from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()
    contract_size = models.IntegerField(default=160)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name

    @property
    def total_cost(self):
        queryset = self.ingredients.all().aggregate(
            total_cost=models.Sum(
                "purchase_price"
            )
        )
        return queryset["total_cost"]
