from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    # 1) Sepet boş mu?
    if not cart_items:
        messages.warning(request, "Sepetiniz boş.")
        return redirect("cart:cart_detail")

    # 2) Önce stok yeterli mi kontrol et
    for item in cart_items:
        if item.product.stock < item.quantity:
            messages.error(
                request,
                f"{item.product.name} için yeterli stok yok."
            )
            return redirect("cart:cart_detail")

    # 3) Order oluştur
    order = Order.objects.create(
        user=request.user,
        total_price=0
    )

    total_price = 0

    # 4) OrderItem oluştur + stok düş
    for item in cart_items:
        line_total = item.get_total_price()

        OrderItem.objects.create(
            order=order,
            product=item.product,
            product_name=item.product.name,
            product_price=item.product.price,
            product_slug=item.product.slug,
            quantity=item.quantity,
            line_total=line_total
        )

        # 5) Stok düş
        product = item.product
        product.stock -= item.quantity
        product.save()

        total_price += line_total

    # 6) Sipariş toplamını güncelle
    order.total_price = total_price
    order.save()

    # 7) Sepeti temizle
    cart_items.delete()

    messages.success(request, "Siparişiniz oluşturuldu!")
    return redirect("orders:success")


@login_required
def success(request):
    return render(request, "orders/success.html")


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)

    total_orders = orders.count()
    pending_count = orders.filter(status="pending").count()
    preparing_count = orders.filter(status="preparing").count()
    shipped_count = orders.filter(status="shipped").count()
    delivered_count = orders.filter(status="delivered").count()

    context = {
        "orders": orders,
        "total_orders": total_orders,
        "pending_count": pending_count,
        "preparing_count": preparing_count,
        "shipped_count": shipped_count,
        "delivered_count": delivered_count,
    }

    return render(request, "orders/my_orders.html", context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()

    context = {
        "order": order,
        "order_items": order_items,
    }
    return render(request, "orders/order_detail.html", context)