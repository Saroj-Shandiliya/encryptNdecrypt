from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.start,name='start'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    url(r'^profile/(?P<rname>\w+)$',views.home,name='Profiles'),
    url(r'^profile/(?P<rname>\w+)/Encrypt',views.encrypt,name='encrypt'),
    url(r'^profile/(?P<rname>\w+)/Message',views.decrypt,name='decrypt'),
    url(r'^profile/(?P<rname>\w+)/Manage',views.manage,name='manage'),
    url(r'^profile/(?P<rname>\w+)/Settings',views.username,name='username'),
    url(r'^profile/(?P<rname>\w+)/About_Us',views.about,name='about'),
    url(r'^profile/(?P<rname>\w+)/Notification',views.notification,name='notification'),
    url(r'^profile/(?P<rname>\w+)/Feedback',views.feedu,name='feedu'),
    url('About_Us/',views.feed,name='About'),
    path('Guest/',views.guest,name='guest'),
    path('Random_guest/',views.randomguest,name='random'),
    path('logout/',views.logout,name='logout'),
    path('forgot_password/',views.forgot,name='forgot'),
    path('Email_verification/',views.verify,name='verify'),
]