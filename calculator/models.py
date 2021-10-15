from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Address(models.Model):

	name = models.CharField(max_length=64, null=False, blank=True)

	house = models.CharField(max_length=255, null=False, blank=False)
	street = models.CharField(max_length=255, null=False, blank=True)

	city = models.CharField(max_length=64, null=False, blank=False)
	state = models.CharField(max_length=64, null=False, blank=False)

	country = models.CharField(max_length=64, null=False, blank=False)
	
	zipcode = models.BigIntegerField(null=False, blank=True)

	slug = models.SlugField(max_length=255, null=False, blank=False, unique=True, default='admin-slug')

	class Meta:
		db_table = 'address'
		unique_together = ('house', 'street', 'city', 'state', 'country', 'zipcode')

	def __str__(self) -> str:
		return f'{self.house}, {self.street}\n{self.city}, {self.state} {self.country}'


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'),)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

	avatar = models.ImageField(upload_to='images/persons', default='images/link.png', null=False, blank=True)

	first_name = models.CharField(max_length=255, null=False, blank=False)
	last_name = models.CharField(max_length=255, null=False, blank=False)

	age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(121)], null=False, blank=False)
	gender = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')

	email = models.EmailField(blank=False, null=False)

	address = models.ManyToManyField(Address, related_name='addresses', blank=True)

	slug = models.SlugField(max_length=255, null=False, blank=False, unique=True, default='admin-slug')

	def is_valid_passenger(self):
		return (self.age > 0 and (len(self.first) + len(self.last)) > 0)

	class Meta:
		db_table = 'person'
		default_related_name = 'User-Person'
		unique_together = ('user', 'email')

	def __str__(self):
		return f'{self.id}. {self.first_name} {self.last_name} {self.age}'
