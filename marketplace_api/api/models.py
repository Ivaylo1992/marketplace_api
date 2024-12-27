from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Product(models.Model):
    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    stock = models.PositiveIntegerField()

    image_field = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    @property
    def in_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.name
    

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pening'
        CONFIRMED = 'Confirmed'
        CANCELED = 'Canceled'
    
    STATUS_MAX_LENGTH = max([len(x) for _, x in StatusChoices.choices])
    
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        choices=StatusChoices.choices 
    )

    product = models.ManyToManyField(
        Product,
        through='OrderItem',
        related_name='orders',
    )

    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"