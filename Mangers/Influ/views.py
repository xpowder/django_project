from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserInfo
from .forms import ProfileForm



@login_required
def create_profile(request):
    # Check if the user already has a profile
    if UserInfo.objects.filter(user=request.user).exists():
        return redirect('profile')  # Redirect to the profile page if the user already has a profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return redirect('profile')  # Redirect to the profile page after successful creation
    else:
        form = ProfileForm()
    
    return render(request, 'create_profile.html', {'form': form})



@login_required
def profile_view(request):
    user_info = get_object_or_404(UserInfo, user=request.user)
    return render(request, 'profile.html', {'user_info': user_info})





def home_page(requset):
    return render(requset, 'home.html', {})

def home(requset):
    return render(requset, 'base.html', {})


@login_required
def profile_edit(request):
    user_info = get_object_or_404(UserInfo, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful save
    else:
        form = ProfileForm(instance=user_info)
    
    return render(request, 'profile_edite.html', {'form': form})
