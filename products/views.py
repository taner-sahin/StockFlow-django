from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)

    return render(request, "products/category_products.html", {
        "category": category,
        "products": products,
    })
    
def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)

    return render(request, "home.html", {
        "categories": categories,
        "products": products,
    })