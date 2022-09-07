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
                    CommentForm,
                    QuestionForm,
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateForm
                )
from .models import  Topics,Questions,Comments
from .forms import TopicsForm
from django.views.generic import DetailView,TemplateView,View
from django.http import HttpResponseRedirect,HttpResponse



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
            return redirect("user_login")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "forum/register.html", context)



def  user_login(request):
    """
      Renders Login Form
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form    = AccountAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are already Logged In")
            return redirect("home")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "forum/login.html", context)

def user_logout(request):  
    logout(request)
    return redirect("home")

def forumhome(request):
    return render(request,'forum/forumhome.html')

def topics(request):
    if request.method == "POST":
        form = TopicsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('topics')
    num_questions = Questions.objects.all().count()   # ?????  how to count correctly
    form = TopicsForm()
    alltopics = Topics.objects.order_by('-date')
    data = {'form':form,'alltopics': alltopics,'num_questions':num_questions}
    
    return render(request,'forum/topics.html',data)


class questionadd(DetailView):
    model = Topics
    template_name = 'forum/onetopic.html'
    context_object_name = 'quest'
    form1 = QuestionForm()
    form2 = CommentForm()
    
    def get(self, request, *args, **kwargs):
        topic = Topics.objects.get(pk=kwargs['pk'])
        form1 = self.form1
        form2 = self.form2
        print('topics')
        for item in Topics.objects.all():
            print(item.pk)

        print('questions')
        for item in Questions.objects.all():
            print(item.pk, item.topic)
        context = {
        'form1': form1,
        'form2': form2,'allquestions':Questions.objects.all(),'topic':topic}
        return render(request, self.template_name, context=context)
    
        # print(500)
        # form1 = self.form1
        # form2 = self.form2
        # return render(request, self.template_name, {'form1': form1,'form2':form2})

    def post(self, request, *args, **kwargs):
        form1 = QuestionForm(request.POST)
        form2 = CommentForm(request.POST)
        if request.method == 'POST' and 'btnaddquestion' in request.POST: 
            if form1.is_valid():
                form1.save(commit=False)
                form1.user = request.user
                form1.save()
                return redirect('exactopic',pk=kwargs['pk'])
        elif request.method == 'POST' and 'comment' in request.POST:          
            if form2.is_valid():
                form2.save(commit=False)
                form2.user = request.user
                form2.save()
                return redirect('exactopic',pk=kwargs['pk'])
        topic = Topics.objects.get(pk=kwargs['pk'])
        context = {
        'form1': form1,
        'form2': form2,'allquestions':Questions.objects.all(),'topic':topic}
        return render(request, self.template_name, context=context)
    















# def questionadd(request,pk):
#     topic=Topics.objects.get(pk=pk)
#     form1 = QuestionForm()
#     form2 = CommentForm()
#     if request.method == "GET":
#         pass
#     if request.method == 'POST' and 'btnaddquestion' in request.POST: 
#         if form1.is_valid():
#                  form1.save()
#                  return redirect('exactopic')
#     if request.method == 'POST' and 'comment' in request.POST:          
#         if form2.is_valid():
#             form2.save()
#             return redirect('exactopic')
#     allquestions = Questions.objects.all()
#     topic=Topics.objects.get(id=id)
#     allcomments = Comments.objects.get(topic=topic)         
#     context = {
#      'form1': form1,
#      'form2': form2,'allquestions':allquestions,'allcomments':allcomments}
#     return render(request, template_name = 'forum/onetopic.html',context=context)
   

        
        
        

    




 
 
