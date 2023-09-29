from django import forms
from .import models


class Creatinganewarticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','slug','intro','body',]