from django.shortcuts import render, redirect
from models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	users = User.objects.all()

	context = {
	"users": users,

	}
	return render(request, 'courseapp/index.html', context)

def create(request):
	did_create = User.objects.user_create(request)

	if did_create:
		return redirect(reverse('course_index'))
	else:
		return redirect(reverse('course_index'))

def delete(request, id):
	user = User.objects.get(id=id)

	user.delete()
	return redirect(reverse('course_index'))

