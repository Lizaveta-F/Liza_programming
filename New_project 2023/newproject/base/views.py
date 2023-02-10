from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseBadRequest, JsonResponse,HttpResponseNotFound
from datetime import datetime as dt
from .forms import UserForm
from .models import Person


# Create your views here.

def home(request):
    people=Person.objects.all()
    return render(request, 'base/home.html',{'people':people})

def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return redirect ('home')
        
def edit(request,pk):
    try:
        person = Person.objects.get(id=pk)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return redirect("home")
        else:
            return render (request, "base/change.html", {'person':person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h1>The person was not found </h1>")
    
def delete(request, pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return redirect("home")
    except Person.DoesNotExist:
        return HttpResponse("This person doesnot exist")