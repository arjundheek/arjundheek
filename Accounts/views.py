from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Profile, ProfileSettings


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/renewal")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="Accounts/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Accounts/login.html", context={"login_form": form})


@login_required(login_url='/login/')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


@login_required(login_url='/login/')
def account_renewal(request):
    profile_settings = ProfileSettings.objects.get(user=request.user)

    template = loader.get_template('Accounts/account-renewal.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def account_delete(request):
    profile_settings = ProfileSettings.objects.get(user=request.user)

    if profile_settings.active == 0:
        return redirect('/renewal')

    template = loader.get_template('Accounts/account-delete.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def delete_user(request):
    profile_settings = ProfileSettings.objects.get(user=request.user)

    if profile_settings.active == 0:
        return redirect('/renewal')

    request.user.delete()

    return redirect('/logout')
