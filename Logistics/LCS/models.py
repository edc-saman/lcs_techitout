from django.db import models


# Create your models here.
# class person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email_address = models.EmailField(max_length=70)
#     mobile = models.IntegerField(max_length=10)


class Supplier(models.Model):
    SupplierName = models.CharField(max_length=200)
    ContactNumber = models.IntegerField()

    def __str__(self):
        return self.SupplierName


class Product(models.Model):
    SupplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.ProductName

class Location(models.Model):
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)

    def __str__(self):
        return self.source

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=70)
    mobile = models.IntegerField(max_length=10)
    address = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
