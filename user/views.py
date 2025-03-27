from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .register_form import registrationForm
from .models import userProfile
from shop.models import Cart
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect("/admin/")
            return redirect("index")
        else:
            return render(request, "user/login.html", {
                "message": "Username or Password is wrong! Please try again"
            })
        
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return render(request, "shop/index.html", {
        "message": "Logged out"
    })

def register_view(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']

            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                
                user_profile = userProfile(
                    user=user,
                    phone_number=phone_number,
                    address=address,
                    gender=gender.lower(),
                    role='customer',
                )
                user_profile.save()

                cart = Cart(user=user)
                cart.save()

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')

            except Exception as e:
                return render(request, 'user/login.html', {
                    'form': form,
                    'message': f"Error during registration: {str(e)}"
                })
        else:
            print(form.errors)
            return render(request, 'user/login.html', {
                'form': form,
                'message': 'Form errors: ' + str(form.errors)
            })
    form = registrationForm()
    return render(request, 'user/login.html', {
        'form': form
    })
    