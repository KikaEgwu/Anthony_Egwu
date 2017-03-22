from django.shortcuts import render, redirect, HttpResponse
import string

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def process(request):
	request.session['data'] = {
		"name": request.POST['name'],
		"location": request.POST['location'],
		"language": request.POST['language'],
		"comment": request.POST['comment']
		}
	return redirect('/result')

def result(request):
	return render(request, 'main/result.html', request.session['data'])