from django.urls import path

from restaurant.views import (
    IndexView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    ToggleAssignToDishView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
    CookExperienceUpdateView,
    IngredientDeleteView,
    IngredientUpdateView,
    IngredientCreateView,
    IngredientDetailView,
    IngredientListView,
    DishTypeDetailView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path("dishtypes/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path(
        "toggle-assign-to-dish/<int:pk>/",
        ToggleAssignToDishView.as_view(),
        name="toggle-dish-assign",
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredient-detail",
    ),
    path(
        "ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
]

app_name = "restaurant"
