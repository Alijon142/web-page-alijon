from django.urls import path
from .views import index_view, alijon,github, Homepage_view,AboutPageView

urlpatterns=[
    path("home", index_view, name='index'),
    path("alijon", alijon, name='alijon'),
    path('github', github, name='github'),
    path('',Homepage_view.as_view(), name='uy'),
    path('about/',AboutPageView.as_view(),name='about')

]