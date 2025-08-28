from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    data = Contact.objects.first()
    return render(request, 'home.html', {'data': data})