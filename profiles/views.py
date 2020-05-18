from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ImageProfileForm
from django.contrib import messages

""" Render the current user Profile page if the user is logged in """
@login_required
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profiles.html', args)


""" Allows the current User to Edit its Profile , Renders edit_profile.html """
@login_required
def edit_profile(request,pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        edit_profile_form = ImageProfileForm(data=request.POST, files=request.FILES, instance=user_profile)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, 'You have successfully updated your profile')
            return redirect('profile')
        else:
            messages.error(request, "Update unsuccessful. Please rectify the problem below")
    else:
        edit_profile_form = ImageProfileForm(instance=user_profile)
    args = {'edit_profile_form':edit_profile_form}
    return render(request, 'edit_profile.html', args)