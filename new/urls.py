from django.urls import path,include
from . import views
from django.conf.urls import url
from django.views import generic
from . import views



app_name="ioe"    #called namespacing of urls,,,so as to distinguish between similar named urls#of different apps
urlpatterns=[
    path(r'home',views.Template.as_view(),name="itsourearth"),
    path('contact',views.contactus,name="contact"),
    path('',views.redirect,name="red"),
    # path('try',views.TryTemplate.as_view(),name="modal"),
]
