# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login,logout
# from . forms import *
# from django.contrib import messages 


# # Create your views here.

# def base(request):
#     return render(request,'forum/base.html')

# def user_login(request):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect ('base')
#         else:
#             messages.error(request,"Invalid username or password")
#     form = AuthenticationForm()
#     context = {
#         'form':form,
#         }  
#     return render(request, 'forum/login.html',context=context)

# def user_logout(request):
#     logout(request)
#     return redirect ('base')
    
# def user_register(request):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect ('user_login')
#     form = UserCreationForm()
#     context = {
#         'form':form,
#         }  
#     return render(request, 'forum/register.html',context=context)
                 
    






















from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import (
                                  authenticate,
                                  logout ,
                                  login
                              )
from django.shortcuts import (
                                  render,
                                  get_object_or_404,
                                  redirect
                              )
from .forms import (
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateform
                )




def base(request):
    """
      Home View Renders base.html
    """
    return render(request, "forum/base.html", {})



def user_register(request):
    """
      Renders Registration Form 
    """
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email    = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password = raw_pass)
            login(request, account)
            messages.success(request, "You have been Registered as {}".format(request.user.username))
            return redirect('base')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "forum/register.html", context)



def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("base")




def  user_login(request):
    """
      Renders Login Form
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("base")
    if request.POST:
        form    = AccountAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("base")
        else:
            messages.error(request,"please Correct Below Errors")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "forum/login.html", context)


def account_view (request):
    """
      Renders userprofile page "
    """
    if not request.user.is_authenticated:
        return redirect("user_login")
    context = {}
    if request.POST:
        form = AccountUpdateform(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form  = AccountUpdateform(
            initial={
            'email':request.user.email,
            'username':request.user.username,
            }
        )
    context['account_form']=form

    return render(request, "forum/userprofile.html",context)




