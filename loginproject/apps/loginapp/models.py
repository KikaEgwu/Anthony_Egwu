from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
	def register(self, request):

		is_valid = True

		if len(request.POST['first_name']) == 0:
			messages.error(request, "First Name is Required")
			is_valid = False

		if len(request.POST['last_name']) == 0:
			messages.error(request, "Last Name is Required")
			is_valid = False

		email_match = User.objects.filter(email=request.POST['email'])

		if len(email_match) > 0:
			messages.error(request, "That email is already is use")
			is_valid = False

		if request.POST['password'] != request.POST['password_confirm']:
			messages.error(request, "The passwords don't match")
			is_valid = False

		if len(request.POST['email']) == 0:
			messages.error(request, "First Name is Required")
			is_valid = False

		if not is_valid:
			print "*"*100
			return False

		hashed = bcrypt.hashpw(request.POST['password'], bcrypt.gensalt())

		new_user = User(
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			pwhash = hashed,
		)
		new_user.save()
		request.session['logged_in_user'] = new_user.id
		print "8"*100
		return True
		

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	pwhash = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()
