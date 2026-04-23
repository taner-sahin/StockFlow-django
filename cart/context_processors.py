from .models import CartItem


def cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        return {"cart_count": total_quantity}

    return {"cart_count": 0}