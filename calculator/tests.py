from django.test import TestCase
from django.urls import reverse

from django.core.management import call_command

from .models import Address, Person
from .import views


# Create your tests here.

class LoginFormTest(TestCase):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'InputFormTest'

class InputFormTest(TestCase):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self):
        return 'InputFormTest'

class ModelsTestCase(TestCase):

	def __init__(self):
		Person = Person(name='test')
		Address = Address()

	def __str__(self) -> str:
		return 'ModelsTestCase'


class UrlsTestCase(TestCase):
	def __str__(self) -> str:
		return 'UrlsTestCase'


class ViewsTestCase(TestCase):

	def test_view_status_code(self):
		self.response = self.client.get(reverse('home'))
		self.assertEqual(self.response.status_code, 200)

	def test_view_template_used_home(self):
		self.response = self.client.get(reverse('home'))
		self.assertTemplateUsed(self.response, 'home.html')
		
	def	__str__(self) -> str:
		return 'ViewsTestCase'

# Test for the templates


class TemplatesTestCase(TestCase):
    def test_validate_templates(self):
        call_command("validate_templates")
