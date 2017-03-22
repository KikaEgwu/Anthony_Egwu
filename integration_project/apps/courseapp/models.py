from __future__ import unicode_literals
from django.contrib import messages
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def user_create(self, request):
		is_valid = True

		if len(request.POST['name']) == 0:
			is_valid = False
			messages.error(request, 'Name is required')

		if len(request.POST['description']) == 0:
			is_valid = False
			messages.error(request, 'Description is required')

		if not is_valid:
			return False

		new_user = User(
			name = request.POST['name'],
			description = request.POST['description'],
			)
		new_user.save()

		return True

class User(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()