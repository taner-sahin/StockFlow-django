from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)

    return render(request, "products/category.html", {
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
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)

    return render(request, "products/detail.html", {
        "product": product,
    })