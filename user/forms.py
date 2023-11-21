from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Profile, CustomUser

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2','phone','address','image','is_staff','date_joined']
        list_display = ['image']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','phone','address','image','is_staff','is_active','date_joined']
        list_display = ['image']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Perform any additional actions before saving, if needed
        if commit:
            user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
    