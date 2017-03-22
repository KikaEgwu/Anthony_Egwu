from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def user_register(self, request):
		is_valid = True

		if len(request.POST['name']) == 0:
			messages.error(request, 'Name is Required')
			is_valid = False

		if len(request.POST['alias']) == 0:
			messages.error(request, 'Alias is Required')
			is_valid = False

		email_match = User.objects.filter(email=request.POST['email'])

		if len(email_match) > 0:
			messages.error(request, "This email is already in use")
			is_valid = False

		if len(request.POST['password']) < 8:
			messages.error(request, 'Password needs to be at least 8 characters long')
			is_valid = False

		if request.POST['password'] != request.POST['confirm_password']:
			messages.error(request, "The passwords don't match")
			is_valid = False

		if not is_valid:
			return False

		hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

		new_user = User(
			name = request.POST['name'],
			alias = request.POST['alias'],
			email = request.POST['email'],
			pwhash = hashed,
			)
		new_user.save()
		request.session['logged_in_user'] = new_user.id
		return True

	def logon(self, request):
		users = User.objects.filter(email=request.POST['email'])

		if len(users) == 0:
			messages.error(request, "User does not exist")
			return False

		user = users[0]

		hashedpw = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.pwhash.encode('utf-8'))

		if hashedpw != user.pwhash:
			messages.error(request, 'Password is incorrect')
			return False

		request.session['logged_in_user'] = user.id
		request.session['username'] = user.name
		return True

	def addbook(self, request):
		is_valid = True

		if len(request.POST['title']) == 0:
			messages.error(request, 'Title is Required')
			is_valid = False

		if len(request.POST['author']) == 0:
			messages.error(request, 'Author is Required')
			is_valid = False

		author_match = Book.objects.filter(author=request.POST['author'])

		if len(author_match) > 0:
			messages.error(request, "The author is already in use")
			is_valid = False

		if len(request.POST['review']) == 0:
			messages.error(request, 'A Review is Required')
			is_valid = False

		if len(request.POST['rating']) == 0:
			messages.error(request, 'Rating must be betwwen 1 and 5')
			is_valid = False

		if not is_valid:
			return False

		new_book = Book(
			title = request.POST['title'],
			author = request.POST['author'],
			review = request.POST['review'],
			rating = request.POST['rating'],
			)
		new_book.save()
		request.session['logged_in_user'] = new_user.id
		return True


class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	pwhash = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()


class Book(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Author(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True) 

class Review(models.Model):
	review = models.TextField()
	rating = models.CharField(max_length=5)
	book = models.ForeignKey(Book)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True) 