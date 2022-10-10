from django.shortcuts import render
from .models import Vacancies, Vacancies_scotland, Vacancies_wales, Vacancies_northireland

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def work_england(request):
    work_england = Vacancies.objects.all()
    query = request.GET.get('q')
    if query:
        work_england = Vacancies.objects.filter(
            Q(title__icontains=query)
        ).distinct()

    paginator = Paginator(work_england, 25)
    page = request.GET.get('page')

    try:
        work_england = paginator.page(page)
    except PageNotAnInteger:
        work_england = paginator.page(1)
    except EmptyPage:
        work_england = paginator.page(paginator.num_pages)

    context = {
        'work_england': work_england
    }
    return render(request, "vacancies/work_england.html", context)


def work_scotland(request):
    search_query = request.GET.get('q')
    vacancies_scotland = Vacancies_scotland.objects.all()
    if search_query:
        vacancies_scotland = Vacancies_scotland.objects.filter(
            Q(title__icontains=search_query)
        ).distinct()

    paginator = Paginator(vacancies_scotland, 25)
    page = request.GET.get('page')

    try:
        vacancies_scotland = paginator.page(page)
    except PageNotAnInteger:
        vacancies_scotland = paginator.page(1)
    except EmptyPage:
        vacancies_scotland = paginator.page(paginator.num_pages)

    data = {
        'vacancies_scotland': vacancies_scotland
    }
    return render(request, 'vacancies/work_scotland.html', data)


def work_wales(request):
    vacancies_wales = Vacancies_wales.objects.all()
    query = request.GET.get('q')
    if query:
        vacancies_wales = Vacancies_wales.objects.filter(
            Q(title__icontains=query)

        ).distinct()

    paginator = Paginator(vacancies_wales, 25)  # 6 posts per page
    page = request.GET.get('page')

    try:
        vacancies_wales = paginator.page(page)
    except PageNotAnInteger:
        vacancies_wales = paginator.page(1)
    except EmptyPage:
        vacancies_wales = paginator.page(paginator.num_pages)

    context = {
        'vacancies_wales': vacancies_wales
    }
    return render(request, "vacancies/work_wales.html", context)


def work_northireland(request):
    vacancies_northireland = Vacancies_northireland.objects.all()
    query = request.GET.get('q')
    if query:
        vacancies_northireland = Vacancies_northireland.objects.filter(
            Q(title__icontains=query)

        ).distinct()

    paginator = Paginator(vacancies_northireland, 25)
    page = request.GET.get('page')

    try:
        vacancies_northireland = paginator.page(page)
    except PageNotAnInteger:
        vacancies_northireland = paginator.page(1)
    except EmptyPage:
        vacancies_northireland = paginator.page(paginator.num_pages)

    data = {
        'vacancies_northireland': vacancies_northireland
    }
    return render(request, 'vacancies/work_northireland.html', data)
