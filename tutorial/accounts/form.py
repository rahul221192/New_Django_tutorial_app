'''
Created on Apr 30, 2017

@author: rahul
'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:  # solved class.Contain metadata of class inside which it resides.
        model = User  # this models comes from User class which is inbuilt in django 
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
        
class EditProfileForm(UserChangeForm): #This is usercreation is extended
    class Meta:
        model=User
        fields=(#fields contain include and there is one more thing called 'exclude' which is used for whatever things which is not required
            'email',
            'first_name',
            'last_name'
            )
        
