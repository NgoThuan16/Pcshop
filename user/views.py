from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .register_form import registrationForm
from .models import userProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect("/admin/")
            return redirect("index")
        else:
            return render(request, "user/login.html", {
                "message": "Username or Password is wrong! Please try again"
            })
    return render(request,'user/login.html')

def register_view(request):
    if request.method == 'POST':
        form = registrationForm(request.POST) 
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            userProfile.objects.create(
                user = user,
                role = 'customer',
                gender=form.cleaned_data['gender'],
                country=form.cleaned_data['country']
            ).save()
            return redirect('login')
        else:
            return render(request, 'user/register.html', {'form': form})
    else:
        form = registrationForm()
    return render(request, 'user/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, "shop/index.html", {
        "message": "Logged out"
    })