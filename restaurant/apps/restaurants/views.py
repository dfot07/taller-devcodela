from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Category, Payment, City, Restaurant

# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kargs):
		context = super(IndexView, self).get_context_data(**kargs)
		context['categories'] = Category.objects.all()
		context['payments'] = Payment.objects.all()
		context['cities'] = City.objects.all()
		restaurants = Restaurant.objects.all()[:5]
		tips = [ restaurant.tip_set.all().count() for restaurant in restaurants]
		context['restaurants'] = zip(restaurants, tips)
		return context