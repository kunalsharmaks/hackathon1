from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "highauth"

urlpatterns = [
	url(r'^$', views.highAuthLogin, name='highAuthLogin'),
	url(r'^ha_loginredirect/', views.ha_LoginRedirect, name='ha_loginredirect'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^dashboard/', views.ha_dashboard, name='ha_dashboard'),
	url(r'^changepassword/', views.ha_dashboard, name='changepassword'),
	url(r'^changepasswordredirect/', views.ChangePasswordRedirect, name='changepasswordredirect'),
	url(r'^addnews/', views.ha_dashboard, name='addnews'),
]
