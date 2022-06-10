from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    title = models.CharField(max_length=50, null='')


class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=256, default='')
    content = models.CharField(max_length=256, default='')
    price = models.CharField(max_length=256, null=False)
    stock = models.CharField(max_length=256, default='')


class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    order_complete = models.CharField(max_length=50, null='')
    pay_complete = models.CharField(max_length=50, default='')
    order_cancel = models.CharField(max_length=50, default='')
    delivery_start = models.CharField(max_length=50, default='')
    delivery_complete = models.CharField(max_length=50, default='')


class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"

    order_count = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)


class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"

    delivery_address = models.CharField(max_length=256, default='')
    address_time = models.CharField(max_length=256, default='')
    discount = models.CharField(max_length=256, default='')
    all_product_price = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.CharField(max_length=256, default='')
    product_count = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
