from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


            messages.success(request, 'Регистрация прошла успешна')
            return redirect('login')

    context = {'form':form}
    return render(request, 'myapp/register.html', context)

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password= password)
        if user.username == 'admin':
            login(request, user)
            return redirect('admin_menu')
        elif user is not None:
            login(request, user)
            return redirect('user_menu')
    context = {}
    return render(request, 'myapp/login.html', context)


def adminMenu(request):
    return render(request, 'myapp/admin_menu.html')


def userMenu(request):
    return render(request, 'myapp/student_menu.html')
