from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ImageProfileForm


@login_required
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profiles.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_profile_form = ImageProfileForm(request.POST, request.FILES, instance=request.user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect(reverse('profile'))
        else:
            form = ImageProfileForm(instance=request.user)
    else:
        edit_profile_form = ImageProfileForm(request.POST, request.FILES)
    args = {'edit_profile_form':edit_profile_form}
    return render(request, 'edit_profile.html', args)