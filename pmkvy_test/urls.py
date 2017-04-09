"""pmkvy_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/districtlist/', views.DistrictList.as_view(), name='api_districtlist'),
    #url(r'^api/customtest/', views.CustomTestList.as_view(), name='api'),
    url(r'^api/candidatelistbasedontrainingcenter/', views.CandidateListBasedOnTrainingCenter.as_view(), name='api_candidatelistbasedontrainingcenter'),
    url(r'^api/trainingcenter/', views.TrainingCenterList.as_view(), name='api_trainingcenter'),
    url(r'^api/candidates/', views.CandidateList.as_view(), name='api_candidate_list'),
    url(r'^api/users/', views.AppUserView.as_view(), name='app_user_view'),
    #url(r'^api/users/(?P<pk>[0-9]+)/$', views.AppUserView.as_view(), name='app_user_view'),
    url(r'^api/logincheck/', views.LoginCheck.as_view(), name='login_check'),
    url(r'^api/singletrainingcenter/', views.SingleTrainingCenter.as_view(), name='single_training_center'),
    url(r'^api/jobroledata/', views.JobRoleData.as_view(), name='api_jobrole'),
    url(r'^api/jobrolesector/', views.JobRoleBasedOnSector.as_view(), name='api_jobrolesector'),
    url(r'^api/coursedata/', views.CourseData.as_view(), name='api_coursedata'),
    url(r'^api/batchinfolist/', views.BatchInfoList.as_view(), name='api_batchinfolist'),
    url(r'^api/fetchtrainingcentercourse/', views.FetchTrainingCenterCourse.as_view(), name='api_fetchtrainingcentercourse'),
    url(r'^api/batchinfocourse/', views.BatchInfoCourse.as_view(), name='api_batchinfocourse'),
    url(r'^api/studentcourselist', views.StudentCourseList.as_view(), name='api_studentcourselist'),
    url(r'^api/getstudentdetails', views.GetStudentDetails.as_view(), name='api_getstudentdetails'),
    url(r'^api/fetchtrainingcenter/', views.fetchtrainingcenteronce.as_view(), name='fetchtrainingcenter'),
    url(r'^api/studentcourseregistrationform', views.StudentCourseRegistrationForm.as_view(), name='api_studentcourseregistrationform'),
    url(r'^api/studentcompletedcourses', views.StudentCompletedCourses.as_view(), name='api_studentcompletedcourses'),
    url(r'^api/studentongoingcourses', views.StudentOngoingCourses.as_view(), name='api_studentongoingcourses'),
    url(r'^api/fetchlocation/', views.fetchtrainingcenteronce, name='fetchlocation'),
    url(r'^api/sendotp/', views.SendOtp.as_view(), name='api_sendotp'),
    #url(r'^api/returncertifiedtraineeList/', views.ReturnCertifiedTraineeList.as_view(), name='returncertifiedtraineeList'),
    url(r'^api/fetchaadhardetail/', views.FetchAadharDetail.as_view(), name='fetchaadhardetail'),
    url(r'^api/trainingcenterbasedonjobrole/', views.TrainingCenterBasedOnJobRole.as_view(), name='api_trainingcenterbasedonjobrole'),
    #url(r'^api/verifyotp/', views.VerifyOtp.as_view(), name='api_verifyotp'),
    url(r'^api/coursefeedback', views.CourseFeedback.as_view(), name='api_coursefeedback'),
    url(r'^api/feedbackstudentcompletedcourses/', views.FeedbackStudentCompletedCourses.as_view(), name='api_feedbackstudentcompletedcourses'),
    #url(r'^trainingcenter/', include("training_center.urls")),
    url(r'^api/candidateregister/', views.CandidateRegister.as_view(), name='api_candidateregister'),
    url(r'^trainingcenter/', include("dashboard_portal.urls")),
    url(r'^api/gpstrainingcenter/', views.GpsTrainingCenterView.as_view(), name='api_gpstrainingcenter'),
    ################ employer urls ############
    url(r'^api/employer/employerregister/', views.EmployerRegister.as_view(), name='employer_employerregister'),
    url(r'^api/employer/employerlogincheck/', views.EmployerLoginCheck.as_view(), name='employer_logincheck'),
    url(r'^api/employer/createjob/', views.CreateJob.as_view(), name='employer_createjob'),    
    #url(r'ha_login/', include("higher_authority.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)