from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Category, Brand, Slide, CartItem, Order, OrderProduct, Review
from .forms import OrderForm, RateForm


def products_list(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()
    category = request.GET.get('category')
    brands = Brand.objects.all()[:3]
    brand = request.GET.get('brand')
    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products
    slides = Slide.objects.all()

    product_id = request.GET.get('product')

    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('product_list')
        for item in cart_item:
            item.quantity += 1
            item.save()

    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "slides": slides,
    }
    return render(request, 'product_list.html', context=context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    if request.user.is_authenticated:
        if not product.view_set.filter(user=request.user).exists():
            product.view_set.create(user=request.user)

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'cart.html', context)


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk).delete()
    return redirect('cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def create_order(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    amount = sum([item.quantity for item in cart_items])
    form = OrderForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price,
            customer=request.user
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price()
            )
        cart_items.delete()
        return redirect('cart')
    return render(request, 'order_creation_page.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form})


def orders(request):
    order_list = Order.objects.filter(customer=request.user)
    context = {
        "orders": order_list,
    }

    return render(request, 'orders.html', context)


def rate_product(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()
            return redirect('rate_product', pk=pk)
    form = RateForm()
    return render(request, 'rate.html', {'form': form, 'product': product, 'reviews': reviews})



















