from django.db import models
from django.utils import timezone


class Users(models.Model):
    # uniqe id for each registered user
    id = models.IntegerField(unique=True, primary_key=True)
    # field for enetring username string
    username = models.CharField(max_length=255)
    # field for entering username password string
    password = models.CharField(max_length=255)
    # field containing username email
    e_mail = models.CharField(max_length=255)
    # field that gets the time of registration
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User: {self.username}, created: {self.created_at}"


class Products(models.Model):
    # unique id for each product registered
    id = models.IntegerField(unique=True, primary_key=True)
    # name of the product
    name = models.CharField(max_length=255)
    # price of the product
    price = models.FloatField()
    # total amount of available products
    quantity = models.IntegerField()
    # time of registration of the product
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.price}. Quantity left: {self.quantity}"


class Categories(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Whishlist(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - {self.name}"


class WhishlistItems(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    whishlist_id = models.IntegerField(unique=True)
    product_id = models.IntegerField()

    def __str__(self):
        return str(self.whishlist_id)


class ProductCategories(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    product_id = models.IntegerField()
    category_id = models.IntegerField()

    def __str__(self):
        return f"{self.product_id} - {self.category_id}"


class Shipments(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    order_id = models.IntegerField()
    tracking_number = models.CharField(max_length=255)
    shipped_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f"{self.order_id} - {self.tracking_number}. Shipped at: {self.shipped_at}"
        )


class Orders(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.IntegerField()
    total_price = models.FloatField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - total price of the orded: {self.total_price}"


class Revievs(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField(default=1)
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Product: {self.product_id} - user: {self.user_id} rated product on {self.rating} at {self.created_at}."


class Adresses(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.IntegerField()
    street_adress = models.CharField(blank=False, max_length=255)
    city = models.CharField(blank=False, max_length=255)
    state = models.CharField(blank=False, max_length=255)
    zip_code = models.CharField(blank=False, max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - Adress: {self.state}, {self.city}, {self.street_adress}, zip code: {self.zip_code}"


class OrderedItems(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.order_id}: containing products - {self.product_id} in quantity of {self.quantity} and total price of {self.price}"
