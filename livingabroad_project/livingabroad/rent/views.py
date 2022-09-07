from django.shortcuts import render
from .models import England_rent, Northireland_rent, Scotland_rent, Wales_rent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.



def england_rent(request):
    england_rent = England_rent.objects.all()
    query = request.GET.get('q')
    if query:
        england_rent = England_rent.objects.filter(
            Q(title__icontains=query)| Q(location__icontains=query)).distinct()

    paginator = Paginator(england_rent, 25)  
    page = request.GET.get('page')

    try:
        england_rent = paginator.page(page)
    except PageNotAnInteger:
        england_rent = paginator.page(1)
    except EmptyPage:
        england_rent = paginator.page(paginator.num_pages)

    context = {
        'england_rent': england_rent
    }
    return render(request, "rent/england_rent.html", context)


def scotland_rent(request):
    scotland_rent = Scotland_rent.objects.all()
    query = request.GET.get('q')
    if query:
        scotland_rent = Scotland_rent.objects.filter(
            Q(title__icontains=query)|Q(location__icontains=query)).distinct()

    paginator = Paginator(scotland_rent, 25) 
    page = request.GET.get('page')

    try:
        scotland_rent = paginator.page(page)
    except PageNotAnInteger:
        scotland_rent = paginator.page(1)
    except EmptyPage:
        scotland_rent = paginator.page(paginator.num_pages)

    context = {
        'scotland_rent': scotland_rent
    }
    return render(request, "rent/scotland_rent.html", context)


def wales_rent(request):
    wales_rent = Wales_rent.objects.all()
    query = request.GET.get('q')
    if query:
        wales_rent = Wales_rent.objects.filter(
            Q(title__icontains=query)|Q(location__icontains=query)).distinct()

    paginator = Paginator(wales_rent, 25)  
    page = request.GET.get('page')

    try:
        wales_rent = paginator.page(page)
    except PageNotAnInteger:
        wales_rent = paginator.page(1)
    except EmptyPage:
        wales_rent = paginator.page(paginator.num_pages)

    context = {
        'wales_rent': wales_rent
    }
    return render(request, "rent/wales_rent.html", context)

def northireland_rent(request):
    northireland_rent = Northireland_rent.objects.all()
    query = request.GET.get('q')
    if query:
        northireland_rent = Northireland_rent.objects.filter(
            Q(title__icontains=query)|Q(location__icontains=query)).distinct()

    paginator = Paginator(northireland_rent, 25)  
    page = request.GET.get('page')

    try:
        northireland_rent = paginator.page(page)
    except PageNotAnInteger:
        northireland_rent = paginator.page(1)
    except EmptyPage:
        northireland_rent = paginator.page(paginator.num_pages)

    context = {
        'northireland_rent': northireland_rent
    }
    return render(request, "rent/northireland_rent.html", context)