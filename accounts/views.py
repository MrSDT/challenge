from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as Mlogin , logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Mlogin(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        login = AuthenticationForm(data=request.POST)
        if login.is_valid():
            user = login.get_user()
            Mlogin(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        login = AuthenticationForm()
    return render(request, 'login.html', {'login': login})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')