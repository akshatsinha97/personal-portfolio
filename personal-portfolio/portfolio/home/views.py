from tkinter import N
from django.shortcuts import render
from home.models import Contact

# Create your views here.

def home(request):
    context = {'name':'Akshat'}
    return render(request,'home.html',context)

def about(request):
    context = {'name':'Akshat'}
    return render(request,'about.html',context)

def projects(request):
    context = {'name':'Akshat'}
    return render(request,'projects.html',context)

def contact(request):
    context = {'name':'Akshat'}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']
        inst = Contact(name=name, email=email, phone=phone, query=query)
        inst.save()
    return render(request,'contact.html',context)