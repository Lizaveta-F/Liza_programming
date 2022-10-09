from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from food.forms import ItemForm
from . models import Item

app_name = 'food'
# Create your views here.

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name: 'item_list'

      

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/add.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    

def update(request, item_id):
    item=Item.objects.get(pk=item_id)
    form=ItemForm(request.POST or None, instance = item )
    if form.is_valid():
        form.save()
        return redirect ('food:index')
    context = {
        'item':item,
        'form':form,
        }
    return render (request, 'food/add.html', context )

def delete(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'GET':
        item.delete()
        return redirect ('food:index')
    context = {
        'item':item,   
    }
    return (request, 'food/detail.html' , context)
    