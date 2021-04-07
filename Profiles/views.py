from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from Home.models import Post
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib import messages

@login_required
def ProfileView(request,*args,**kwargs):
    username=kwargs.get('username')
    user_=User.objects.filter(username=username).first()
    posts=Post.objects.filter(author=user_)


    return render(request, 'Profiles/profile.html', context={'user_':user_,'posts':posts})

@login_required
def UpdateProfileView(request):
    if(request.method=='POST'):
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            messages.success(request,'Profile saved successfully')
            return redirect('profile_view',username='Siddhant')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    return render(request,'Profiles/profile_update.html',context={'u_form':u_form,'p_form':p_form})
