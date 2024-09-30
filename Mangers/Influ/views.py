from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserInfo
from .forms import ProfileForm



@login_required
def create_profile(request):
    if UserInfo.objects.filter(user=request.user).exists():
        return redirect('profile')  

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return redirect('profile') 
        form = ProfileForm()
    
    return render(request, 'create_profile.html', {'form': form})



@login_required
def profile_view(request):
    user_info = get_object_or_404(UserInfo, user=request.user)
    return render(request, 'profile.html', {'user_info': user_info})





def home(request):
    user_info = None
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
    
    return render(request, 'base.html', {
        'user_info': user_info,
    })




def view_profile(requset):
    form = get_object_or_404(UserInfo, user=requset.user)
    return render(requset, 'view_profile.html', {'form' : form })

@login_required
def profile_edit(request):
    user_info = get_object_or_404(UserInfo, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm(instance=user_info)
    
    return render(request, 'profile_edite.html', {'form': form})
