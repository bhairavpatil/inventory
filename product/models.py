from django.db import models

from category.models import Category
# Create your models here.

class Product(models.Model):
	"""For product categories"""
	name = models.CharField(max_length=100)
	desc = models.TextField()
	priceperitem = models.IntegerField(max_length=10)
	quantity = models.IntegerField(max_length=10)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)


	def __str__(self):
		return self.name


from django.contrib import admin
