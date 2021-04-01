from django.test import TestCase

# Create your tests here.

class LoginFormTest(tests.TestCase):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'InputFormTest'

class InputFormTest(TestCase):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self):
        return 'InputFormTest'
