from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from WebTraining.customer_profile.forms import ProfileForm
from WebTraining.customer_profile.models import Profile


@login_required
def customer_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProfileForm(instance=profile)
        context = {
        'form': form,
        }

        return render(request, 'customer_profile.html', context)