from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import User, Review, Book
# Create your views here.
def index(request):
	return render(request, 'beltapp/index.html')

def register(request):
	did_register = User.objects.user_register(request)

	if did_register:
		return redirect(reverse('dashboard'))
	else:
		return redirect(reverse('index'))

def logon(request):
	did_login = User.objects.logon(request)

	if did_login:
		return redirect(reverse('dashboard'))
	else:
		return redirect(reverse('index'))

def logout(request):
	return render(request, 'beltapp/index.html')

def dashboard(request):
	users = User.objects.all()

	books = Book.objects.all()

	reviews = Review.objects.all()

	context = {

		"users": users,
		"books": books,
		"reviews": reviews,
		}
	return render(request, 'beltapp/dashboard.html', context)

def addbook(request):
	did_addbook = Book.objects.addbook(request)

	if did_addbook:
		return redirect(reverse('dashboard'))
	else:
		return redirect(reverse('addingbook'))

def addingbook(request):
	users = User.objects.all()

	books = Book.objects.all()

	reviews = Review.objects.all()

	context = {

		"users": users,
		"books": books,
		"reviews": reviews,
		}
	return render(request, 'beltapp/books.html', context)

def addreview(request):
	did_addreview = Review.objects.addreview(request)

	if did_addreview:
		return redirect(reverse('dashboard'))
	else:
		return redirect(reverse('addingbook'))