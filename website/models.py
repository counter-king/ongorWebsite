from django.db import models

# Create your models here.
class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='menu_images/')
	price = models.DecimalField(max_digits=10, decimal_places=0)
	category = models.ManyToManyField('Category', related_name='item')

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class OrderModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=25, decimal_places=0)
	items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
	name = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return f'Order: {self.created_on.strftime("%b, %d, %I:, %M, %p")}'

class GalleryModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='gallery_images/')

	def __str__(self):
		return f'Image: {self.created_on.strftime("%b, %d, %I:, %M, %p")}'
