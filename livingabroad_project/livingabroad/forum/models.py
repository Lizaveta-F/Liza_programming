import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse

#manager for our custom model 
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class 
    """
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    
    """
      Custom user class inheriting AbstractBaseUser class 
    """
    
    email                = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username             = models.CharField(max_length=30,unique=True)
    date_joined          = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login           = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=True)
    is_staff             = models.BooleanField(default=False)
    is_superuser         = models.BooleanField(default=False)
   


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True
    
    
class Topics(models.Model):
    
    topic = models.CharField(max_length=100)
    date = models.DateField("Date of publication", default=datetime.date.today)
    slug=models.SlugField(max_length=100,blank=True,editable=False)
    user = models.ForeignKey(Account,blank=True, null=True,on_delete=models.SET_NULL)

    ordering = ('-date',)
    def __str__(self):
        return self.topic
    
    def save(self, *args, **kwargs):       
        self.slug = slugify(self.topic)
        super(Topics, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('exactopic', kwargs={'topic_slug': self.slug})

    
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        
        
       
        
class Questions(models.Model):
    
    topic = models.ForeignKey(Topics,blank=True, null=True,on_delete=models.CASCADE,related_name='quests')
    question = models.CharField(max_length=200)
    date = models.DateField("Date of publication", default=datetime.date.today)
    user = models.ForeignKey(Account,blank=True, null=True,on_delete=models.SET_NULL)
    slug=models.SlugField(max_length=200,blank=True,editable=False)
    
    ordering = ('-date',)
    
    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):       
        self.slug = slugify(self.topic)
        super(Questions, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('exactquestion', kwargs={'question_slug': self.slug, 'topic_slug':self.topic.slug})
    
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        
class Comments(models.Model):
    
    topic = models.ForeignKey(Topics,blank=True, null=True,on_delete=models.CASCADE,related_name='commentstop')
    slug=models.SlugField(max_length=400,blank=True,editable=False)
    question = models.ForeignKey(Questions,blank=True, null=True,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField(max_length=400)
    date = models.DateField("Date of publication", default=datetime.date.today)
    user = models.ForeignKey(Account,blank=True, null=True,on_delete=models.SET_NULL)

    ordering = ('-date',)
    
    def __str__(self):
        return self.comment
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super(Comments, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"