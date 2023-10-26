from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import DishForm, IngredientForm
from .models import DishType, Cook, Dish, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "years_of_experience",
                        "contract_size",
                    )
                },
            ),
        )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                        "contract_size",
                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    form = DishForm
    search_fields = ("name",)
    list_filter = ("cooks",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    form = IngredientForm
    search_fields = ("name",)
    list_filter = ("dishes",)


admin.site.register(DishType)
