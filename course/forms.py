from django import forms
from .models import Signup

# class studentForms(forms.Form):
#     name = forms.CharField(label='Full Name',max_length=100)


# class RegistrationForm(forms.Form):
#     firstname = forms.CharField(label='First Name' , max_length=100, widget=forms.TextInput(attrs={'class':'form-contro w-100'}))
#     lastname = forms.CharField(label='Last Name' , max_length=100, widget = forms.TextInput(attrs={'class':'form-control w-100'}))
#     email = forms.EmailField(label='Email', widget = forms.TextInput(attrs={'class':'form-control w-100'}))
#     password = forms.CharField(label='Create Password', max_length=100, widget=forms.
#     PasswordInput(attrs={'class':'form-control w-100'}))
#     password1 = forms.CharField(label='confirm password', max_length=100, widget=forms.
#     PasswordInput(attrs={'class':'form-control w-100'}))


class studentForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"


