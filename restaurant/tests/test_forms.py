from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormsTests(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "username": "new.user",
            "password1": "usertest123",
            "password2": "usertest123",
            "first_name": "Test first_name",
            "last_name": "Test second_name",
            "years_of_experience": 10,
        }

    def test_cook_creation_form_with_years_of_experience_is_valid(self):
        form = CookCreationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.cleaned_data, self.valid_form_data)

    def test_invalid_years_of_experience_formats(self):
        invalid_formats = ["ABC12", "12o345678", "abc12345", "ABCccccc"]

        for invalid_years_of_experience in invalid_formats:
            with self.subTest(invalid_years_of_experience=invalid_years_of_experience):
                form_data = self.valid_form_data.copy()
                form_data["years_of_experience"] = invalid_years_of_experience
                form = CookCreationForm(data=form_data)
                self.assertFalse(form.is_valid())
                self.assertIn("years_of_experience", form.errors)
