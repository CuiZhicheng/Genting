from django.db import models
from django import forms
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class GentingUserManager(BaseUserManager):
	def create_user(self, username, email, password):
		if not email: raise ValueError('GentingUsers must have a valid email.')
		if not username: raise ValueError('GentingUsers must have a valid username.')
		if not password: raise ValueError('GentingUsers must have a valid password.')
		GentingUser = self.model(username = username, email=email)
		GentingUser.set_password(password)
		GentingUser.save(using=self._db)
		print 'Create User'
		return GentingUser

	def create_superuser(self, username, email, password):
		GentingUser = self.create_user(username, email, password)
		GentingUser.is_admin = True
		GentingUser.save(using=self._db)
		return GentingUser


class UserProfile(AbstractBaseUser):
	USERNAME_MSG = 'Username must consist of digits, letters, underscores and hyphens only, and between 2 to 20 characters.'
	username = models.CharField(max_length = 20, unique = True, 
		validators = [RegexValidator(regex = r'[\w\-][\w\-]+', message = USERNAME_MSG)])

	email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = GentingUserManager()

    # User Information
	score = models.FloatField(default=0)
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def __str__(self): 
		return self.username

	def is_staff(self): 
		return self.is_admin
	
	def has_perm(self, perm, obj=None):
		return self.is_staff()

	def has_module_perms(self, app_label):
		return True
	

class UploadForm(forms.Form):
	desc = forms.CharField(max_length=500)
	img = forms.ImageField()

class Picture(models.Model):
	user = models.ForeignKey(UserProfile)

	img = models.ImageField(upload_to='img/')
	pub_date = models.DateTimeField('date published', auto_now_add=True)

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