from django.urls import path
from .views import Homepage_view,AboutPageView

urlpatterns=[
    path('homepage/',Homepage_view.as_view(), name='homepage'),
    path('',AboutPageView.as_view(),name='about')
]