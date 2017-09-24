from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from jchart import Chart
import json
import requests

from api.models import TrainingCenter, AppUser, StudentCourseRegistration
from api.models import TrainingCenterCourse, TrainingCenterJobRole
from api.models import BatchInfo, CandidateRegistration, StudentCourseRegistration, CourseInfo

from api.serializers import StudentCourseRegistrationSerializer
"""
Render login page for training center
"""
localhost = 'http://localhost:8001'

def centerLoginPage(request):
	if request.session.get('center_id'):
		return HttpResponseRedirect('/trainingcenter/updatedetail/')
	else:
		return render(request, 'dashboard_portal/login.html')


def LoginRedirect(request):

	if request.session.get('center_id'):
		return HttpResponseRedirect("/dashboard/")
	else:
		tc_obj = TrainingCenter.objects.get(center_id=request.POST['center_id'])
		print("HELlo")
		if tc_obj.password == request.POST['password']:
			request.session['center_id'] = tc_obj.center_id
			return HttpResponseRedirect("/trainingcenter/updatedetail/")
		else:
			return HttpResponseRedirect('/trainingcenter/')

def ChangePassword(request):

	if request.session.get('center_id'):
		return render(request, 'dashboard_portal/changepassword.html')
	return HttpResponse(True)

def ChangePasswordRedirect(request):

	if request.session.get('center_id'):
		tc_obj = TrainingCenter.objects.get(center_id=request.session['center_id'])
		if tc_obj.password == request.POST['oldpassword']:
			tc_obj.password = request.POST['newpassword']
			tc_obj.save()
		else:
			return HttpResponseRedirect('/test_delete')
	else:
		return HttpResponseRedirect('/test_delete')
	return HttpResponseRedirect('/dashboard/')
"""
def trainingCenterLogin(request):          ##dashboard

	url = "http://9a3a0b42.ngrok.io/api/singletrainingcenter/"

	center_id = request.POST["centerid"]

	data = {
		"center_id":center_id
	}

	response = requests.post(url, data=data)
	#return HttpResponse(response.text)
	if (response.text == "false") or (response.text == "False") and (request.session.get("center_id", None)):
		return HttpResponseRedirect("/tc_login/")
	else:
		request.session['center_id']=center_id
		jsonobject = json.loads(response.text)

		finalresult = jsonobject["data"]
		return HttpResponseRedirect(reverse("/tc_login/dashboard/", args=(center_id,)))

		#return render(request, 'pmkvy_test/dashboard.html', {'result':finalresult})
"""
def UpdateDetailView(request):

	try:
		if request.session.get('center_id'):
			center_id = request.session['center_id']
		else:
			#return HttpResponseRedirect('/tc_login/')
			center_id = request.POST["centerid"]
	except:
		return HttpResponseRedirect('/trainingcenter/')

	tc_obj = TrainingCenter.objects.get(center_id=center_id)
	result = {
		'training_center_name':tc_obj.training_center_name,
		'center_id':center_id,
		'address':tc_obj.address,
		'training_partner':tc_obj.training_partner,
		'center_poc_name':tc_obj.center_poc_name,
		'center_poc_email':tc_obj.center_poc_email
	}

	return render(request, 'dashboard_portal/update_training_center.html', {'result':result})

def Update(request):
	try:
		if request.session.get('center_id'):
			center_id = request.session['center_id']
		else:
			return HttpResponseRedirect('/trainingcenter/')
	except:
		return HttpResponseRedirect('/trainingcenter/')

	tc_obj = TrainingCenter.objects.get(center_id=center_id)
	tc_obj.training_center_name = request.POST.get('c_name')
	#print(request.POST.get('c_name'))
	tc_obj.address = request.POST.get('c_addr')
	tc_obj.training_partner = request.POST.get('c_partner_name',"")
	tc_obj.center_poc_email = request.POST.get('c_poc_email',"")
	tc_obj.center_poc_name = request.POST.get('c_poc_name',"")
	tc_obj.save()
	#tc

	return HttpResponseRedirect("/trainingcenter/updatedetail/")

def logout(request):
	if request.session.get('center_id'):
		del request.session['center_id']
		return HttpResponseRedirect("/trainingcenter")
	else:
		return HttpResponse("Please Login First")


def all_courses(request):
	if request.session.get('center_id'):
		courselist = []
		center_id = request.session.get('center_id')
		tc_id = TrainingCenter.objects.get(center_id=center_id)
		c_datalist = TrainingCenterCourse.objects.filter(training_center_id=tc_id)
		#jsonobject = json.dumps(datalist)
		for center in c_datalist:
			result = {
				'c_id':center.course_id
			}

			courselist.append(result)
		return render(request, 'dashboard_portal/allcourse.html', {'result':courselist})

def addnewcourse(request):

	return render(request, 'dashboard_portal/addnewcourse.html')


def listallstudents(request):
	if request.session.get("center_id"):
		center_id = request.session.get("center_id")
		url = "http://localhost:8000/api/candidatelistbasedontrainingcenter/"
		data = {
			"center_id":center_id
		}
		response = requests.post(url, data=data)
		jsonobject = json.loads(response.text)
		print(response.text)
		return render(request, 'dashboard_portal/listallstudents.html', {'result':jsonobject})


def addnewstudent(request):
	if request.session.get('center_id'):
		return render(request, 'dashboard_portal/addnewstudent.html')
	else:
		return HttpResponseRedirect('/trainingcenter/')

def addnewstudentprocess(request):
	if request.session.get('center_id'):
		c_name = request.POST['c_name']
		c_email_id = request.POST['c_email_id']
		c_contact_number = request.POST['c_contact_number']
		c_address = request.POST['c_address']
		c_state_ut = request.POST['c_state_ut']
		c_district = request.POST['c_district']
		c_pincode = request.POST['c_pincode']
		c_date_of_birth = request.POST['c_date_of_birth']
		c_f_name = request.POST['c_f_name']
		c_gender = request.POST['c_gender']
		c_category = request.POST['c_category']
		c_annual_family_income = request.POST['c_annual_family_income']
		c_educational_qualification = request.POST['c_educational_qualification']
		c_preferred_training_state_ut = request.POST['c_preferred_training_state_ut']
		c_sector = request.POST['c_sector']
		c_course = request.POST['c_course']
		c_max_fee = request.POST['c_max_fee']
		c_app_user_email = request.POST['c_app_user_email']

		c_obj = CandidateRegistration.objects.create(c_name=c_name, c_email_id=c_email_id, c_contact_number = c_contact_number, c_address = c_address, c_state_ut = c_state_ut, c_district = c_district, c_pincode = c_pincode, c_date_of_birth = c_date_of_birth, c_f_name = c_f_name, c_gender = c_gender, c_category = c_category, c_annual_family_income = c_annual_family_income, c_educational_qualification = c_educational_qualification, c_preferred_training_state_ut = c_preferred_training_state_ut, c_sector = c_sector, c_course = c_course, c_max_fee = c_max_fee, c_app_user_email = c_app_user_email)
		return HttpResponse(True)
	else:
		return HttpResponseRedirect('/trainingcenter/')

def editstudent(request):
	if request.session.get("center_id"):
		return render(request, 'dashboard_portal/editstudent.html')
	else:
		return HttpResponseRedirect('/trainingcenter/')

def editstudentprocess(request):
	if request.session.get("center_id"):
		try:
			c_app_user_email = request.POST["c_app_user_email"]
			student_obj = CandidateRegistration.objects.get(c_app_user_email=c_app_user_email)
			return render(request, 'dashboard_portal/editstudent.html', {'result':student_obj})
		except:
			return HttpResponseRedirect('/trainingcenter/')

def editstudentprocess1(request):
	if request.session.get("center_id"):
		c_app_user_email = request.POST["c_app_user_email"]
		student_obj = CandidateRegistration.objects.get(c_app_user_email=c_app_user_email)
		return render(request, 'dashboard_portal/editstudent.html', {'result':student_obj})

def addnewbatch(request):
	if request.session.get("center_id"):
		return render(request, 'dashboard_portal/addnewbatch.html')
	else:
		return HttpResponseRedirect("/trainingcenter/")

def addnewbatchprocess(request):
	if request.session.get("center_id"):
		training_center_id = request.session.get("center_id")
		tc_obj = TrainingCenter.objects.get(center_id=training_center_id)
		course_id = request.POST["course_id"]
		course_obj = CourseInfo.objects.get(course_id=course_id)
		batch_start_date = request.POST["batch_start_date"]
		batch_end_date = request.POST["batch_end_date"]
		#ch_assessment_date = request.POST["batch_assessment_date"]

		batch_obj = BatchInfo.objects.create(training_center_id=tc_obj, course_id=course_obj, batch_start_date=batch_start_date, batch_end_date=batch_end_date)
		return HttpResponse(True)
	else:
		return HttpResponseRedirect("/trainingcenter/")
"""
def editbatchdetail(request):
	if request.session.get("center_id"):
		return render(request, 'dashboard_portal/editbatchdetail.html')
	else:
		return HttpResponseRedirect("/trainingcenter/")

def editbatchdetailprocess(request):
	if request.session.get("center_id"):

"""
"""
def dashboardPortal(request):
	url = "http://9a3a0b42.ngrok.io/api/singletrainingcenter/"

	center_id = request.session['center_id']
	data = {
		"center_id":center_id
	}

	response = requests.post(url, data=data)
	#return HttpResponse(response.text)
	jsonobject = json.loads(response.text)
	print(jsonobject)
	finalresult = jsonobject["data"]
	request.session['alldata'] = jsonobject
	return render(request, 'pmkvy_test/dashboard.html', {'result':finalresult})
"""
def updateCenterInfo(request):

	if not request.session['alldata']:
		c_name = request.POST["c_name"]
		c_id = request.POST["c_id"]
		c_address = request.POST["c_addr"]
		c_partner_name = request.POST["c_partner_name"]
		c_poc_name = request.POST["c_poc_name"]
		c_poc_email = request.POST["c_poc_email"]
	"""
	else:
		c_name = request.session["alldata"]["c_name"]
		c_id = request.session["alldata"]["c_id"]
		c_address = request.session["alldata"]["c_addr"]
		c_partner_name = request.session["alldata"]["c_partner_name"]
		c_poc_name = request.session["alldata"]["c_poc_name"]
		c_poc_email = request.session["alldata"]["c_poc_email"]
	"""
	training_center = TrainingCenter.objects.get(center_id=c_id)

	training_center.training_center_name = c_name
	training_center.address = c_address
	#training_center.training_partner = c_partner_name
	training_center.center_poc_name = c_poc_name
	training_center.center_poc_email = c_poc_email
	training_center.save()

	#return HttpResponseRedirect('/tc_login/dashboard/')
	dashboardView(request)
	#return render(request, 'pmkvy_test/dashboard.html', {'updateresult':'Updated Successfully'})

"""
Students list module for training center dashboard
students register under that training center
"""
def StudentsList(request):
	if request.session.get('center_id'):
		tc_obj = TrainingCenter.objects.get(center_id=request.session['center_id'])
		student_list = StudentCourseRegistration.objects.filter(scr_training_center_id=tc_obj)
		return render(request, 'dashboard_portal/studentslist.html', {'student_list' : student_list})
	return HttpResponse("You need to login first")



def ManageBatches(request):
	if request.session.get('center_id'):
		tc_obj = TrainingCenter.objects.get(center_id=request.session['center_id'])
		batch_list = BatchInfo.objects.filter(training_center_id=tc_obj)
		return render(request, 'dashboard_portal/managebatches.html', {'batch_list':batch_list})
	return HttpResponse("You need to login first")

def AddNewsAndNotice(request):
	return render(request, 'dashboard_portal/addnewsandnotice.html')

def HigherAuthority(request):
	response = requests.get(localhost +'/api/trainingcenterfeedback/')
	jsonobject = json.loads(response.text)
	neg_list = jsonobject['neg_list']
	no_neg = len(neg_list)
	pos_list = jsonobject['pos_list']
	no_pos = len(pos_list)
	neg_percent = float(no_neg)/(no_neg+no_pos)*100
	pos_percent = float(no_pos)/(no_neg+no_pos)*100
	data = []
	data.append(pos_percent)
	data.append(neg_percent)
	# return render(request, 'dashboard_portal/higherauthority.html', {'no_neg':no_neg, 'no_pos':no_pos, 'neg_percent':neg_percent, 'pos_percent':pos_percent})
	return render(request, 'dashboard_portal/higherauthority.html', {'data': data})
