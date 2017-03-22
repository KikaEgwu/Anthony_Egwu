from django.shortcuts import render, redirect
from models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	return render(request, "loginapp/index.html")


def register(request):
	did_register = User.objects.user_register(request)

	if did_register:
		return redirect(reverse("login_dashboard"))
	else:
		return redirect(reverse('login_index'))

def login(request):
	did_login = User.objects.login(request)

	if did_login:
		return redirect(reverse('login_dashboard'))
	else:
		return redirect(reverse('login_index'))

def dashboard(request):
	users = User.objects.all()

	books = Book.objects.all()

	reviews = Review.objects.all()

	context = {

		"users": users,
		"books": books,
		"reviews": reviews,
	}
	return render(request, 'loginapp/dashboard.html', context)