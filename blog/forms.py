from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post,Study


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'desc']
#         labels = {'title': 'Title', 'desc': 'Description'}
#         widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
#                    'desc': forms.Textarea(attrs={'class': 'form-control'}), }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['title', 'desc','url1','url2','url3','url4','image']
        labels = {'title': 'Title', 'desc': 'Description','url1':'First step','url2':'Second step','url3':'Third step','url4':'Fourth step'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control'}),
                   'url1': forms.URLInput(attrs={'class': 'form-control'}),
                   'url2': forms.URLInput(attrs={'class': 'form-control'}),
                   'url3': forms.URLInput(attrs={'class': 'form-control'}),
                   'url4': forms.URLInput(attrs={'class': 'form-control'}),
                   'image': forms.FileInput()
                   
                   }