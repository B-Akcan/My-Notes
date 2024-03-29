from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.info(request, f"Account created for {username}.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    
    return render(request, "users/register.html", {"form":form})