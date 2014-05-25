from django.db import models
import django

<<<<<<< HEAD
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class GentingUserManager(BaseUserManager):
	def create_user(self, email, date_of_birth, password):
		if not email: raise ValueError('GentingUsers must have a valid email.')
		if not date_of_birth: raise ValueError('GentingUsers must have a valid date_of_birth.')
		if not password: raise ValueError('GentingUsers must have a valid password.')
		GentingUser = self.model(email=email, date_of_birth = date_of_birth)
		GentingUser.set_password(password)
		GentingUser.save(using=self._db)
		return GentingUser

	def create_superuser(self, email, date_of_birth, password):
		GentingUser = self.create_user(email, date_of_birth, password)
		GentingUser.is_admin = True
		GentingUser.save(using=self._db)
		return GentingUser


class UserProfile(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
	date_of_birth = models.DateField()
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = GentingUserManager()

    # User Information
	score = models.FloatField(default=0)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth']

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __str__(self): 
		return self.email

	def is_staff(self): 
		return self.is_admin
	
	def has_perm(self, perm, obj=None):
		return self.is_staff()

	def has_module_perms(self, app_label):
		return True
	

class Picture(models.Model):
	user = models.ForeignKey(UserProfile)
=======
class UserProfile(models.Model):
	# Foreign Key to User
	user = models.ForeignKey(django.contrib.auth.models.User)

	# User Information
	score = models.FloatField(default=0)


class Picture(models.Model):
	user = models.ForeignKey(django.contrib.auth.models.User)
>>>>>>> f5fb75f4c6f15bba916aae9b29706c8d2dc11ec8

	img = models.ImageField(upload_to='img/')
	pub_date = models.DateTimeField('date published')

	text = models.CharField(max_length=500)
	score = models.FloatField(default=0)
	#comment = models.ForeignKey(django.contrib.comments.models.Comment)


class Location(models.Model):
	picture = models.ForeignKey(Picture)

	num = models.IntegerField()
	street = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	#zipcode = models.ForeignKey(Zipcode)
	#objects = models.GeoManager()

"""
class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()()

    objects = models.GeoManager()
"""