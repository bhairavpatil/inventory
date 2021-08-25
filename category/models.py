from django.db import models

# Create your models here.

class Category(models.Model):
	"""For product categories"""
	name = models.CharField(max_length=100)
	desc = models.TextField()


	def __str__(self):
		return self.name