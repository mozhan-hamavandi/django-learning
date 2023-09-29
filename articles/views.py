from django.shortcuts import render,redirect
from .models import Article
from .import forms

from django.http import HttpResponse

# Create your views here.

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,"articles/article_list.html",{'articles':articles})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})
   
def article_create(request):
    if request.method =='POST':
        form = forms.Creatinganewarticle(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('articles:list')      
    form = forms.Creatinganewarticle()
    return render(request,'articles/article_creat.html',{'form':form})
