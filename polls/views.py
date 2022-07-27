from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
from django.utils.translation import gettext_lazy as _

from django.contrib import messages
import json


def pet_form(request):
    form = PetForm
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pet = form.save()
            return JsonResponse({"msg": "Pet successfully saved.", "pet_name": name})
        else:
            return JsonResponse({"msg": "Invalid data", "pet_name": None})
    else:
        form = PetForm()
        return render(request, 'create.html', {"form": form})
