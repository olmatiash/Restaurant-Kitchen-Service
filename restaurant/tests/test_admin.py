from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import Cook


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.cook = Cook.objects.create(
            username="cook", password="testcook", years_of_experience=5
        )

    def test_cook_years_of_experience_listed(self):
        """
        This test checks whether the "years of experience" value of a Cook is displayed
        correctly on the admin page for cooks.
        """
        url = reverse("admin:restaurant_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        """
        This test is meant to verify if the "years of experience" is listed
        on the detailed change page for a Cook in the admin site.
        """
        url = reverse("admin:restaurant_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_add_years_of_experience_listed(self):
        """
        This test is designed to ensure that the "years_of_experience" field is present
        in the "add" page when creating a new Cook in the admin site.
        """
        url = reverse("admin:restaurant_cook_add")
        res = self.client.get(url)
        self.assertContains(res, "years_of_experience")
