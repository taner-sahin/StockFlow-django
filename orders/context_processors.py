from .models import Order


def order_count(request):
    if request.user.is_authenticated:
        count = Order.objects.filter(user=request.user).count()
        return {"order_count": count}

    return {"order_count": 0}