from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(min_value=16,required=True, widget=forms.NumberInput(attrs={"class":"myfield"}))
