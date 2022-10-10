from django.shortcuts import render
from . models import Order, Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Product.objects.all()
    
    search_text = request.GET.get('search_text')
    if search_text != '' and search_text is not None:
        product_objects = product_objects.filter(title__icontains = search_text)
        
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    context = {
        'product_objects': product_objects,
    }
    return render (request,'shop/index.html', context)

def detail(request, id):
    product_object = Product.objects.get(pk=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

def checkout(request):
    
    if request.method == "POST":
        items = request.POST.get("items","")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        adress = request.POST.get("adress", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip = request.POST.get("zip", "")
        total = request.POST.get ("total", "")
        
        order = Order(items=items,name=name,email=email,adress=adress, city=city,state=state,zip=zip, total=total)
        order.save()
    
    return render(request, 'shop/checkout.html')