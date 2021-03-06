from django.test import TestCase
from .models import categories, technologies, colors, countries
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.

class categoriesTestClass(TestCase):
    def setUp(self):
        self.Art = categories(categories='Education')

    def test_instance(self):
        self.assertTrue(isinstance(self.Art, categories))

    def tearDown(self):
        categories.objects.all().delete()

    def test_save_method(self):
        self.Art.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.Art.delete_category('Education')
        category = categories.objects.all()
        self.assertTrue(len(category) == 0)


class technologiesTestClass(TestCase):
    def setUp(self):
        self.Python = technologies(technologies='Javascript')

    def test_instance(self):
        self.assertTrue(isinstance(self.Python, technologies))

    def tearDown(self):
        technologies.objects.all().delete()

    def test_save_method(self):
        self.Python.save_technology()
        technology = technologies.objects.all()
        self.assertTrue(len(technology) > 0)

    def test_delete_method(self):
        self.Python.delete_technology('Javascript')
        technology = technologies.objects.all()
        self.assertTrue(len(technology) == 0)


class countriesTestClass(TestCase):
    def setUp(self):
        self.Kenya = countries(countries='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, countries))

    def tearDown(self):
        countries.objects.all().delete()

    def test_save_method(self):
        self.Kenya.save_country()
        country = countries.objects.all()
        self.assertTrue(len(country) > 0)

    def test_delete_method(self):
        self.Kenya.delete_country('Kenya')
        country = countries.objects.all()
        self.assertTrue(len(country) == 0)
