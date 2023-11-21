from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .models import CustomUser
#from django.contrib.flatpages.views import flatpage
#import logging
#logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account registered for {username}. Continue to Login')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html',context)

def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            #print("Forms are valid")
            p_form.save()
            u_form.save()
            #print("Data saved")
            #return redirect('user-profile')
            return HttpResponseRedirect(reverse('user-profile'))
        #else:
            #logger.debug("Form validation failed")
            #logger.debug("User form errors: %s", u_form.errors)
            #logger.debug("Profile form errors: %s", p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    #logger.debug("Rendering profile_update.html")
    return render(request, 'user/profile_update.html', context)
    #return flatpage(request,'user/profile_update.html', context)
