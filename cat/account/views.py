from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm



# Create your views here.

def  account(request):
   return render(request,'account/lo_rg.html')



def register(request):
    if request.method == "POST":
        form =  (request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")  # Redirect after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, "register.html", {"form": form})

def success(request):
    return render(request, "success.html")

