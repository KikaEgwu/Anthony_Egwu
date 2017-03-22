from django.shortcuts import render, redirect
import random, string
# Create your views here.

def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, 'main/index.html')
def word(request):
	if request.method == 'POST':
		request.session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		request.session['count'] += 1
	return redirect('/')