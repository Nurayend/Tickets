from django.shortcuts import render, redirect
from .forms import createUserForm, searchForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'api/index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'api/about.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createUserForm()
        if request.method == 'POST':
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You have successfully registered!')
                return redirect('login')
        context = {'form': form}
        return render(request, 'api/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'api/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
