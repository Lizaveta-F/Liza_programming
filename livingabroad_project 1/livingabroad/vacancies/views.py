from django.shortcuts import render
from .models import Vacancies, Vacancies_scotland, Vacancies_wales, Vacancies_northireland

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginatorfunc(queryset,request):
    paginator = Paginator(queryset,25)
    page = request.GET.get('page')
    try:
       queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    return {'paginator':paginator, 'page':page, 'queryset':queryset}


def work_england(request):
    work_england = Vacancies.objects.all()
    query = request.GET.get('q')
    if query:
        work_england = Vacancies.objects.filter(
            Q(title__icontains=query)
        ).distinct()
    context = paginatorfunc(work_england,request)
    return render(request, "vacancies/work_england.html", context)


def work_scotland(request):
    search_query = request.GET.get('q')
    vacancies_scotland = Vacancies_scotland.objects.all()
    if search_query:
        vacancies_scotland = Vacancies_scotland.objects.filter(
            Q(title__icontains=search_query)
        ).distinct()

    context = paginatorfunc(vacancies_scotland,request)
    return render(request, 'vacancies/work_scotland.html', context)


def work_wales(request):
    vacancies_wales = Vacancies_wales.objects.all()
    query = request.GET.get('q')
    if query:
        vacancies_wales = Vacancies_wales.objects.filter(
            Q(title__icontains=query)

        ).distinct()

    context = paginatorfunc(vacancies_wales,request)
    return render(request, "vacancies/work_wales.html", context)


def work_northireland(request):
    vacancies_northireland = Vacancies_northireland.objects.all()
    query = request.GET.get('q')
    if query:
        vacancies_northireland = Vacancies_northireland.objects.filter(
            Q(title__icontains=query)

        ).distinct()

    context = paginatorfunc(vacancies_northireland, request)
    return render(request, 'vacancies/work_northireland.html', context)
