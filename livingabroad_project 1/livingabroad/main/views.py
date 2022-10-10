from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main/Front.html')
def exploreGB(request):
    return render(request,'main/GB.html')
def england(request):
    return render(request,'main/England.html')
def scotland(request):
    return render(request,'main/Scotland.html')
def wales(request):
    return render(request,'main/Wales.html')
def northernireland(request):
    return render(request,'main/NorIreland.html')
def shopping(request):
    return render(request,'main/shopping.html')
def studyinengland(request):
    return render(request,'main/Englandstudy.html')
def studyinscotland(request):
    return render(request,'main/Scotlandstudy.html')
def studyinwales(request):
    return render(request,'main/Walestudy.html')
def studyinnorireland(request):
    return render(request,'main/NorIrelandstudy.html')





# Отвечает за методы, которые будут вызваны при переходе пользователя на определённую страницу