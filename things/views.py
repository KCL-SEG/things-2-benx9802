from django.shortcuts import render
from .forms import ThingForm
from .models import Thing
from datetime import datetime

def home(request):
    
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            print("SAVED")
            form_input = form.cleaned_data
            new_thing = Thing(
                name=form_input['name'],
                description = form_input['description'],
                quantity = form_input['quantity']
            )
            try:
                new_thing.save()
            except:
                print("ERROR")
                return render(request, 'home.html', {'form': form})
        else:
            print("NONE")
            return render(request, 'home.html', {'form': form})

    form = ThingForm()
    return render(request, 'home.html', {'form': form})
