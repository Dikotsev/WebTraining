from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

# Create your views here.
from WebTraining.web_training_auth.forms import SignInForm, SignUpForm


def sign_up(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()
    context = {
        'form': form,
        }
    return render(request, 'auth_template/sign up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form
    }
    return render(request, 'auth_template/sign in.html', context)



def sign_out(request):
    logout(request)
    return redirect('index.html')
