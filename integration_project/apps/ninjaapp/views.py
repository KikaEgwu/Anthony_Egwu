from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ninjaapp/index.html')
def ninjas(request):
	context = {
	"leonardo": True,
	"michelangelo": True,
	"donatello": True,
	"raphael": True,
	"megan": False,
	}
	return render(request, 'ninjaapp/ninjas.html', context)

def one_ninja(request, color):
	context = {
	"leonardo": False,
	"michelangelo": False,
	"donatello": False,
	"raphael": False,
	"megan": False,
	}

	if color == "blue":
		context["leonardo"] = True
	elif color == "red":
		context["raphael"] = True
	elif color == "orange":
		context["michelangelo"] = True
	elif color == "purple":
		context["donatello"] = True
	else:
		context["megan"] = True
	return render(request, 'ninjaapp/ninjas.html', context)