from django.shortcuts import render, redirect
from models import Product, Review
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	products = Product.objects.all()

	context = {
		"products": products,
	}
	return render(request, "productsapp/index.html", context)

def product_create(request):
	did_create = Product.objects.product_create(request)

	if did_create:
		return redirect(reverse('product_index')) # to success
	else:
		return redirect(reverse('product_index')) # back to form

def product_show(request, id):
	product = Product.objects.get(id=id)
	review = Review.objects.filter(product=product)
	context = {
		"product": product,
	}
	return render(request, "productsapp/product_show.html", context)

def product_edit(request, id):
	product = Product.objects.get(id=id)
	context = {
		"product": product,
	}
	return render(request, "productsapp/product_edit.html", context)

def product_update(request, id):
	product = Product.objects.get(id=id)
	#validation
	product.name = request.POST['name']
	product.price = request.POST['price']
	product.description = request.POST['description']

	product.save()
	return redirect(reverse('product_show', kwargs={'id': id}))
	# return redirect("/products/"+id)

def product_delete(request, id):
	product = Product.objects.get(id=id)
	product.delete()

	return redirect('product_index')

def review_create(request):
	print "*"*50
	print request.POST

	did_create = Review.objects.review_create(request)
	return redirect("/products/"+request.POST['product_id'])