from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.utils import timezone

# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(121)], null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    profile_image = models.ImageField(upload_to='images/')
    zipcode = models.BigIntegerField(null=False, blank=True)

    user = models.ForeignKey(User, on_delete=cascade, )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
