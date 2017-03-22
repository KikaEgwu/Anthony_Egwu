from django.shortcuts import render, redirect
import random, string
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, 'main/index.html')
def word(request):
	if request.method == 'POST':
		request.session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
		request.session['count'] += 1
	return redirect(reverse('word_index'))

def reset(request):
	if request.method == 'POST':
		request.session['word'] = ""
		request.session['count'] = 0
	return redirect(reverse('word_index'))