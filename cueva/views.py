from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout 
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            return render(request, 'signin/signin.html', {'form': form, 'error': 'Invalid credentials.'})
    else:
        form = AuthenticationForm()
    return render(request, 'signin/signin.html', {'form': form})



    
def signout(request):
    logout(request)
    return redirect('home') 


def home(request):
    return render(request, 'home.html')



 


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

 
@login_required
def category_list(request):
    
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def products_by_category(request, category_id): 
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'products_by_category.html', {'products': products})
 





@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})