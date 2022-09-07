from email.policy import default
from xmlrpc.client import DateTime
from .models import Articles
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons' , 'full_text', 'date']
        
        widgets = {
            "title":TextInput(attrs={'class':'form-control', 'placeholder':'Name of article'}),
            "anons":TextInput(attrs={'class':'form-control', 'placeholder':'Anons of article'}),
            "date":DateTimeInput(attrs={'class':'form-control','placeholder':'Date of publication', default:'7.08.2022'}),
            "full_text":Textarea(attrs={'class':'form-control','placeholder':'Text of article'})   
        }