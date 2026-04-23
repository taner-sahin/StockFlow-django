from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.models import CartItem


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
    product = get_object_or_404(Product, slug=slug)

    cart_quantity = 0

    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(
            user=request.user,
            product=product
        ).first()

        if cart_item:
            cart_quantity = cart_item.quantity

    can_add_to_cart = product.stock > cart_quantity

    context = {
        "product": product,
        "cart_quantity": cart_quantity,
        "can_add_to_cart": can_add_to_cart,
    }

    return render(request, "products/detail.html", context)