from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import OrderModel, Category, MenuItem, GalleryModel

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		send_mail(
			message_subject + ' raqamidan xabar!',
			message,
			message_email,
			['ungorchoyxona@gmail.com'],
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name':message_name})
	else:
		return render(request, 'contact.html', {})

# def order(request):
# 	return render(request, 'order.html', {})

class Order(View):
	def get(self, request, *args, **kwargs):

		#get every item from each category
		ordered_meals = MenuItem.objects.filter(category__name__contains='Buyurtma_Taom')
		drinks = MenuItem.objects.filter(category__name__contains='Ichimlik')

		#pass into context
		context = {
			'ordered_meals': ordered_meals,
			'drinks': drinks
		}

		#render the template
		return render(request, 'order.html', context)


	def post(self, request, *args, **kwargs):

		name = request.POST.get('name')
		phone = request.POST.get('phone')
		address= request.POST.get('address')
		

		order_items = {
			'items': [],
		}

		items = request.POST.getlist('items[]')

		for item in items:
			
			menu_item = MenuItem.objects.get(pk__contains=int(item))
			item_data = {
				'id': menu_item.pk,
				'name': menu_item.name,
				'price': menu_item.price,
			}

			order_items['items'].append(item_data)

			price = 0
			quantity = 0

			item_ids = []

		for item in order_items['items']:
			quantity = request.POST.get('quantity')
			result = item['price'] * int(quantity)
			price += result
			# price += item['price'] * int(quantity)
			item_ids.append(item['id'])


			order = OrderModel.objects.create(
				price=price,
				name=name,
				phone=phone,
				address=address
				)
			order.items.add(*item_ids)

			context = {
				'items': order_items['items'],
				'price': price,
				'quantity': quantity
			}

		return render(request, 'order_confirmation.html', context)

class Gallery(ListView):
	model = GalleryModel
	template_name = 'gallery.html'




