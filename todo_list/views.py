from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages
# from django.http import HttpResponseRedirect

def home(request):
		if request.method == "POST":
				form = ListForm(request.POST or None)

				if form.is_valid():
						form.save()
						all_items = List.objects.all
						messages.success(request, ('Item has been added to the list!'))
						return render(request, 'home.html', {'all_items': all_items})		
		else:
				all_items = List.objects.all
				return render(request, 'home.html', {'all_items': all_items})

def about(request):
		return render(request, 'about.html', {})

def delete(request, list_id):
		item = List.objects.get(pk=list_id)
		item.delete()
		messages.success(request, ('Item has been deleted!'))
		return redirect('home')

def complete(request, list_id):
		item = List.objects.get(pk=list_id)
		item.completed = True
		item.save()
		messages.success(request, ('Item has been completed!'))
		return redirect('home')

def uncomplete(request, list_id):
		item = List.objects.get(pk=list_id)
		item.completed = False
		item.save()
		messages.success(request, ('Item marked back as uncomplete!'))
		return redirect('home')

def edit(request, list_id):
		if request.method == "POST":
				item = List.objects.get(pk=list_id)
				form = ListForm(request.POST or None, instance=item)

				if form.is_valid():
						form.save()
						messages.success(request, ('Item has been edited!'))
						return redirect('home')
		else:
				item = List.objects.get(pk=list_id)
				return render(request, 'edit.html', {'item': item})
		