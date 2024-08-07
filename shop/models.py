from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=70)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('Category', default=False, on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', default=None, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default_product.png', null=True, upload_to='product_img'
    )

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='brand_img')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class View(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    total_price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order # %s' % (str(self.id))


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amount, self.order.customer.username)


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Perfect'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return self.user.username
