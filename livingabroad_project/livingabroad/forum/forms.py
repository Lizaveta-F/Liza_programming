from xmlrpc.client import DateTime
from django import forms
from .models import Account, Comments, Questions,Topics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,TextInput,DateTimeInput

class RegistrationForm(UserCreationForm):
    """
      Form for Registering new users 
    """
    email = forms.EmailField(max_length=60)
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  Account
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

class AccountUpdateForm(forms.ModelForm):
    """
      Updating User Info
    """
    class Meta:
        model  = Account
        fields = ('email', 'username')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' already in use." % username)

        
class TopicsForm(ModelForm):
    topic = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                "placeholder": "Define a topic ...",
                                "class": "textarea ",
                                }
                                ),
                                label="",)
    
    class Meta:
        model = Topics
        fields = ['topic']
        
class QuestionForm(ModelForm):
    question = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                "placeholder": "Ask a question ...",
                                "class": "textarea ",
                                }
                                ),
                                label="",)
    
    class Meta:
        model = Questions
        fields = ['question']
        
        
class CommentForm(ModelForm):
    comment = forms.CharField(required=True,widget=forms.widgets.Textarea(
                                attrs={
                                "placeholder": "You can leave your comment here ...",
                                "class": "textarea1 ",
                                }
                            ),
                                label="",
                        )
    
    class Meta:
        model = Comments
        fields = ['comment']
        
        
        
        
       