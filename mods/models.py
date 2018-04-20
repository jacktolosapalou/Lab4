from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(primary_key=True, max_length = 100)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	userOb = models.Manager()



class Cart(models.Model):
	cartCode = models.IntegerField()
	cartPrice = models.FloatField()
	cartPaid = models.NullBooleanField()
	cartOb = models.Manager()


class Product(models.Model):
	productPrice = models.FloatField()
	productName = models.CharField(max_length = 100)
	productDesc = models.CharField(max_length = 100)
	productOb = models.Manager()