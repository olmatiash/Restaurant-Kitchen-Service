from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType, Dish, Cook, Ingredient

DISH_TYPES_URL = reverse("restaurant:dish-type-list")
DISH_URL = reverse("restaurant:dish-list")
COOK_URL = reverse("restaurant:cook-list")
INGREDIENT_URL = reverse("restaurant:ingredient-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        """Test that Dish Type list is not displayed when
        we are not logged in"""
        response = self.client.get(DISH_TYPES_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        """Test displaying Dish Type list when we logged in
        and views using correct template"""
        DishType.objects.create(name="test name")
        DishType.objects.create(name="test name1")
        response = self.client.get(DISH_TYPES_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_type_list"]), list(dish_types))
        self.assertTemplateUsed(response, "restaurant/dishtype_list.html")

    def test_search_dish_type_by_name(self):
        """Test that we can find Dish Type by name"""
        DishType.objects.create(name="test name")
        search_name = "test name"
        response = self.client.get(DISH_TYPES_URL, {"name": search_name})
        context_dish_type = DishType.objects.filter(name__icontains=search_name)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["dish_type_list"], context_dish_type)


class PublicCookTest(TestCase):
    def test_login_required(self):
        """Test that Cook list is not displayed where
        we are not logged in"""
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="cook12345", years_of_experience=84
        )
        self.client.force_login(self.cook)

    def test_retrieve_cook(self):
        """Test displaying Cook list when we logged in
        and views using correct template"""
        Cook.objects.create(username="test")
        response = self.client.get(COOK_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "restaurant/cook_list.html")

    def test_search_cook_by_name(self):
        """Test that we can find Cook by name"""
        Cook.objects.create(username="test1")
        Cook.objects.create(username="test2")
        search_name = "test"
        response = self.client.get(COOK_URL, {"username": search_name})
        context_cook = Cook.objects.filter(username__icontains=search_name)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(context_cook),
        )


class PublicDishTest(TestCase):
    def test_login_required(self):
        """Test that Dish list is not displayed where
        we are not logged in"""
        response = self.client.get(DISH_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "qaz123", "QWE12345")
        self.client.force_login(self.user)

    def test_retrieve_cook(self):
        """Test displaying Dish list when we logged in
        and views using correct template"""
        dish_type = DishType.objects.create(name="test name")
        Dish.objects.create(
            name="test name", description="testdesc", price=10.50, dish_type=dish_type
        )
        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "restaurant/dish_list.html")


class PublicIngredientTest(TestCase):
    def test_login_required(self):
        """Test that Ingredient list is not displayed where
        we are not logged in"""
        response = self.client.get(INGREDIENT_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateIngredientTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "qaz123", "QWE12345")
        self.client.force_login(self.user)

    def test_retrieve_cook(self):
        """Test displaying Ingredient list when we logged in
        and views using correct template"""
        Ingredient.objects.create(
            name="test name", provider="testprov", unit="1kg", purchase_price=6.50
        )
        response = self.client.get(INGREDIENT_URL)
        ingredients = Ingredient.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["ingredient_list"]), list(ingredients))
        self.assertTemplateUsed(response, "restaurant/ingredient_list.html")
