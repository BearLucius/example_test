from django.shortcuts import render

# Создание страниц делается в views

def home(request):
    return render(request, 'main/home.html')
