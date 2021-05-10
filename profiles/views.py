from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from . import forms, models


@login_required(login_url='/accounts/login')
def user_profile(request):
    data = models.UpdateInfo.objects.all()
    return render(request, 'userprofile.html', {'data': data})


class UserEditProfile(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'usersettings.html'
    success_url = reverse_lazy('userprofile.html')

    def get_object(self):
        return self.request.user


def information(request):
    if request.method == 'POST':
        form = forms.Info(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:userprof')
    else:
        form = forms.Info()
    return render(request, 'info.html', {'form': form})