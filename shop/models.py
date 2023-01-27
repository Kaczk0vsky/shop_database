from django.db import models
from django.utils import timezone

# Explaining how basic field parameters work:
#
# unique = True - you cannot assaing for example another id which is equal to any existing id of that instance in database
# primery_key = True - it means that, that field is used as id in sql datatable
# editable = False - you cannot edit this field through django admin panel and it isnt visible aswell
# max_length - max length of data string passed to field
# default - setting default value as <smth>
# db_column - custom name of database column
# blank = True/False - means that field might be blank/cannot be blank
# on_delete - specifies what happens to database after deleting object
#


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"User {self.id}: {self.username}, created: {self.created_at}"


class Product(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Reviev(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id"
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    rating = models.IntegerField(default=1)
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.user_id} rated products on {self.rating} at {self.created_at}."


class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id"
    )
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column="category_id"
    )

    def __str__(self):
        return f"{self.product_id} - {self.category_id}"


class Whishlist(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.user_id} - {self.name}"


class WhishlistItem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    whishlist_id = models.ForeignKey(
        Whishlist, on_delete=models.CASCADE, db_column="wishlist_id"
    )
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id"
    )

    def __str__(self):
        return f"{self.id} - {self.whishlist_id}"


class Order(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    total_price = models.FloatField(
        max_length=10, editable=False, blank=True, null=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.user_id} - total price of the orded: {self.total_price}"


class OrderedItem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column="order_id")
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id"
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order_id}: containing products - {self.product_id} in quantity of {self.quantity} and total price of {self.price}"


class Adress(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    street_adress = models.CharField(blank=False, max_length=255)
    city = models.CharField(blank=False, max_length=255)
    state = models.CharField(blank=False, max_length=255)
    zip_code = models.CharField(blank=False, max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.user_id} - Adress: {self.state}, {self.city}, {self.street_adress}, zip code: {self.zip_code}"


class Shipment(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column="order_id")
    user_adress = models.ForeignKey(
        Adress, on_delete=models.CASCADE, db_column="user_adress"
    )
    tracking_number = models.CharField(max_length=255, unique=True, editable=False)
    shipped_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return (
            f"{self.order_id} - {self.tracking_number}. Shipped at: {self.shipped_at}"
        )
