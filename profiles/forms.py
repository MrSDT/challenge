
from django import forms

from .models import UpdateInfo


class Info(forms.ModelForm):
    class Meta:
        model = UpdateInfo
        fields = ['realname' , 'age', 'desc']