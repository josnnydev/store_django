from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import redirect
from .form import ProductForm



def home(request):
    return render(request, 'home.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

 

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def products_by_category(request, category_id): 
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'products_by_category.html', {'products': products})
 





def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})