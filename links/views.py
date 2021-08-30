from django.shortcuts import render, redirect
from .models import Link
from .forms import AddLinkForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home_view(request):
	error = None
	no_discounted = 0

	form = AddLinkForm(request.POST or None)

	if request.method == 'POST':
		try:
			if form.is_valid():
				form.save()
		except AttributeError:
			error = "Couldn't get the price and name, Sorry"
		except:
			error = "Something is not working."

	form = AddLinkForm()


	qs = Link.objects.all()
	total_item = qs.count()
	discount_link = []

	if total_item > 0:
		for item in qs:
			if item.old_price > item.current_price:
				discount_link.append(item)
				no_discounted = len(discount_link)

	context = {

	'form': form,
	'no_discounted':no_discounted,
	'error': error,
	'qs': qs,
	'total_item': total_item

	}

	return render(request, 'links/main.html', context)

class DeleteLinkView(DeleteView):
	model = Link
	template_name = 'links/delete_link.html'
	success_url = reverse_lazy("home-view")

def update_view(request):
	obj = Link.objects.all()

	for link in obj:
		link.save()
	return redirect("home-view")

