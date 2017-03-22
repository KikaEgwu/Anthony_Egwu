from __future__ import unicode_literals
from django.contrib import messages
from django.db import models

# Create your models here.
class ProductManager(models.Manager):
	def product_create(self, request):

		#validation

		is_valid = True

		if len(request.POST['name']) == 0:
			is_valid = False
			messages.error(request, 'Name is required')

		if len(request.POST['description']) == 0:
			is_valid = False
			messages.error(request, 'Description is required')

		#if validation fails, return false

		if not is_valid:
			return False

		#put it in the db


		new_product = Product(
			name = request.POST['name'],
			description = request.POST['description'],
			price = request.POST['price'],
			)
		new_product.save()

		#return true
		return True

class ReviewManager(models.Manager):
	def review_create(self, request):
		# validation
		product = Product.objects.get(id=request.POST['product_id'])
		new_review = Review(
			product = product,
			description = request.POST['description'],
			)
		new_review.save()
		return True

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ProductManager()

class Review(models.Model):
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	product = models.ForeignKey(Product)
	objects = ReviewManager()
