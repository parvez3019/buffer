from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):
	title = "Welcome"



	form = SignUpForm(request.POST or None)
	
	context = {
		"title" : title,
		"form": form,
	}
	

	if form.is_valid():
		form.save()
		context = {
			"title":"Thankyou"
		}
	

	return render(request,"home.html",context)