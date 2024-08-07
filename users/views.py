from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, SignInForm, EditProfileForm, ChangePasswordForm


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    form = SignUpForm()
    context = {"form": form}
    return render(request, 'sign_up.html', context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    form = SignInForm()
    context = {"form": form}
    return render(request, 'sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('sign_in')


def edit_profile(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    form = EditProfileForm(instance=request.user)
    context = {
        "form": form
    }
    return render(request, 'edit_profile.html', context)


def reset_password(request):
    form = ChangePasswordForm(request.user, request.POST)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('sign_in')
    form = ChangePasswordForm(request.user)
    context = {
        "form": form
    }
    return render(request, 'reset_password.html', context)
