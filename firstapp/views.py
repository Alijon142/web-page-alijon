from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


class Homepage_view(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


def homepage_view(request):
    return  HttpResponse('Hello World')

def index_view(request):
    return render(request, 'index.html')


def alijon(request):
    return HttpResponse("<a href='https://t.me/Settings'><image src='https://yandex.ru/images/search?pos=0&from=tabbar&img_url=http%3A%2F%2Fb-h-c.ru%2Flocal%2Ftemplates%2Fbrickhouse-new%2Fimg%2Ftg-main.png&text=telegram&rpt=simage&lr=10335'></a>")

def github(request):
    return HttpResponse("<h1><a href='http://github.com'> github </h1>")