from msilib.schema import ListView
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
from django.db.models import Count,Q



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
    questions = Topics.objects.annotate(questions_count=Count('quests')) 
    form = TopicsForm()
    alltopics = Topics.objects.all().order_by('-date')
    data = {'form':form,'alltopics': alltopics,'questions':questions}
    
    return render(request,'forum/topics.html',data)


class questionadd(DetailView):
    model = Topics
    template_name = 'forum/onetopic.html'
    context_object_name = 'quest'
    form1 = QuestionForm()
    
    def get(self, request, topic_slug):     
        topic = get_object_or_404(Topics, slug=topic_slug)
        queryset = topic.quests.all()
        form1 = self.form1        
        context = {
        'form1': form1,'allquestions':Questions.objects.filter(topic=topic.pk),'topic':topic,'queryset':queryset}
        return render(request, self.template_name, context=context)
    

    def post(self, request, topic_slug):
        
        form1 = QuestionForm(request.POST)
        if request.method == 'POST' and 'btnaddquestion' in request.POST: 
            topic = Topics.objects.get(slug=topic_slug)
            
            if form1.is_valid():
                question = form1.save(commit=False)
                question.user = request.user
                question.topic = topic
                question.save()
                return redirect('exactopic',topic_slug=topic_slug)
            
        context = {
        'form1': form1,'allquestions':Questions.objects.filter(topic=topic.pk),'topic':topic}
        return render(request, self.template_name, context=context)
    



class commentadd(DetailView):
    model = Questions
    template_name = 'forum/onequestion.html'
    context_object_name = 'comms'
    form2 = CommentForm()
    
    def get(self, request, question_slug,topic_slug):
        topic = get_object_or_404(Topics, slug=topic_slug)
        question = Questions.objects.filter(slug=question_slug).first()
        
        form2 = self.form2       
        context = {
        'form2': form2,'allcomments':Comments.objects.filter(question=question.pk),'question':question,
        'topic':topic}
        return render(request, self.template_name, context=context)
    

    def post(self, request, question_slug,topic_slug):
        form2 = CommentForm(request.POST)
        topic = Topics.objects.get(slug=topic_slug)
        question = Questions.objects.filter(slug=question_slug).first()
        if request.method == 'POST' and 'commentbtn' in request.POST: 
            if form2.is_valid():
                comment = form2.save(commit=False)
                comment.user = request.user
                comment.question = question
                # question.topic = topic
                comment.topic = topic
                comment.save()
                return redirect('exactquestion',question_slug=question_slug,topic_slug=topic_slug)           
        context = {
        'form2': form2,'allcomments':Comments.objects.filter(question=question.pk),
        'topic':topic,'question':question}
        return render(request, self.template_name, context=context)







        
        
        

    




 
 
