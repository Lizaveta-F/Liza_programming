from django.shortcuts import render,redirect
from . models import Food, Consume
# Create your views here.

def index(request):
    
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name = food_consumed)
        user = request.user
        consume = Consume(user = user, food_consumed = consume)
        consume.save()
        food = Food.objects.all()
    else:
        food = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
        
    return render(request,'calories_main/index.html',{'food':food, 'consumed_food': consumed_food})

def delete_consumed(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect ('/')
    else:
        return render ( request, 'calories_main/delete.html')