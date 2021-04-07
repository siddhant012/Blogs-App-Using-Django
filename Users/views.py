from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def RegisterView(request):
    if(request.method=='POST'):
        form=UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('post_list_view')
    else:
        form=UserRegisterForm()
    
    return render(request,template_name='Users/register.html',context={'form':form})

