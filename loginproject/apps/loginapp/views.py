from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
	return render(request, "loginapp/index.html")


def register(request):
	did_register = User.objects.register(request)

	if did_register:
		return redirect("/dashboard")
	else:
		return redirect("/login")