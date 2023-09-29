from django.contrib import admin
from django.urls import path
from django.urls import include,re_path
from .import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$',views.articles_list,name="list"),
    re_path(r'^create/', views.article_create, name="create"),

    path('<slug:slug>/',views.article_detail,name="detail"),

]