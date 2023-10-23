from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish, Ingredient


class ModelsTests(TestCase):
    def test_dish_type_format_str(self):
        """
        This test checks if the str representation of a DishType object matches its name attribute.
        """
        dish_type = DishType.objects.create(name="test")
        self.assertEquals(str(dish_type), dish_type.name)

    def test_cook_str(self):
        """
        This test creates a Cook object and verifies that the str representation
        of the object follows the expected format,
        including the username, first name, and last name.
        """
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            years_of_experience=5,
            contract_size=160,
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        """
        This test creates a Dish object and checks if the str representation of
        the object is the same as its name attribute.
        """
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(name="Test", price=10.50, dish_type=dish_type)
        self.assertEqual(str(dish), dish.name)

    def test_create_cook_years_of_experience(self):
        """
        This test creates a Cook object and asserts that the attributes like username,
        years_of_experience, and password are correctly assigned.
        """
        username = "test"
        password = "test123"
        years_of_experience = 5
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=5,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))

    def test_ingredient_str(self):
        """
        This test creates an Ingredient object and checks if the str representation of
        the object is the same as its name attribute.
        """
        ingredient = Ingredient.objects.create(name="testname", provider="market", unit="100g", purchase_price=5.50)
        self.assertEqual(
            str(ingredient), f"{ingredient.name} "
                             f"({ingredient.provider} "
                             f"{ingredient.unit} "
                             f"{ingredient.purchase_price})"
        )
