from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "dashboard"

urlpatterns = [
	url(r'^$', views.centerLoginPage, name='login'),
	url(r'^loginredirect/', views.LoginRedirect, name='loginredirect'),
	#url(r'^portal/', views.trainingCenterLogin, name='trainingcenterlogin'),
	url(r'^updatedetail', views.UpdateDetailView, name='updatedetail'),
	url(r'^update/', views.Update, name='update'),
	url(r'^allcourse/', views.all_courses, name='allcourse'),
	url(r'^addnewcourse/', views.addnewcourse, name='addnewcourse'),
	url(r'^listallstudents/', views.listallstudents, name='listallstudents'),
	url(r'^addnewstudent/', views.addnewstudent, name='addnewstudent'),
	url(r'^editstudent/', views.editstudent, name='editstudent'),
	url(r'^editstudentprocess/', views.editstudentprocess, name='editstudentprocess'),
	url(r'^editstudentprocess1/', views.editstudentprocess1, name='editstudentprocess1'),
	url(r'^addnewstudentprocess/', views.addnewstudentprocess, name='addnewstudentprocess'),
	url(r'^addnewbatch/', views.addnewbatch, name='addnewbatch'),
	url(r'^addnewbatchprocess/', views.addnewbatchprocess, name='addnewbatchprocess'),
	#url(r'^dashboard/updated/', views.updateCenterInfo, name='update'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^studentslist/', views.StudentsList, name='studentslist'),
	url(r'^managebatches/', views.ManageBatches, name='managebatches'),
	url(r'^addnews/', views.AddNewsAndNotice, name='addnews'),
	url(r'^changepassword/', views.ChangePassword, name='changepassword'),
	url(r'^changepasswordredirect/', views.ChangePasswordRedirect, name='changepasswordredirect'),
]