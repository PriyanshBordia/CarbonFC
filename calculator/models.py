from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Address(models.Model):

	name = models.CharField(max_length=64, null=False, blank=False)

	address = models.CharField(max_length=255, null=False, blank=False)
	address2 = models.CharField(max_length=255, null=False, blank=True)

	city = models.CharField(max_length=64, null=False, blank=False)
	state = models.CharField(max_length=64, null=False, blank=False)

	country = models.CharField(max_length=64, null=False, blank=False)
	
	zipcode = models.BigIntegerField(null=False, blank=True)

	class Meta:
		db_table = 'address'

	def __str__(self) -> str:
		return f'{self.address},\n{self.address2}\n{self.city}, {self.state}'


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'),)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

	profile = models.ImageField(upload='images/person')

	first_name = models.CharField(max_length=255, null=False, blank=False)
	last_name = models.CharField(max_length=255, null=False, blank=False)

	age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(121)], null=False, blank=False)
	sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')

	email = models.EmailField(blank=False, null=False)

	address = models.ManyToManyField(Address, related_name='addresses', blank=True)

	avatar = models.ImageField(upload_to='images/', default='images/link.png', null=False, blank=True)
	avatar_thumbnail = ImageSpecField(source='avatar', processors=[ResizeToFill(100, 50)], format='PNG', options={'quality': 60})

	ph_no = models.BigIntegerField(blank=True, null=False, default=0000000, unique=True)

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', default=0)

	def is_valid_passenger(self):
		return (self.age > 0 and len(self.first) + len(self.last) > 0)

	class Meta:
		db_table = 'person'
		default_related_name = 'User-Persons'
		managed = False

	def __str__(self):
		return f'{self.first_name} {self.last_name} {self.age}'
