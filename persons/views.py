# views.py
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons_list')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})

def redirect_to_add_person(request):
    return redirect('add_person')
