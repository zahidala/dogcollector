from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.

# class Dogs:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# dogs = {
#     Dogs('Fido', 'German Shepherd', 'long coat', 3),
#     Dogs('Bella', 'Husky', 'thick coat', 5),
#     Dogs('Daisy', 'Golden Retriever', 'brown coat', 1)
# }

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})