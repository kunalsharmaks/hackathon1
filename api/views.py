from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
import json

from .models import CustomTest, TrainingCenter, TrainingCenterCourse
from .models import CandidateRegistration, AppUser, JobRole, SectorSkillCouncil
from .models import CourseInfo, BatchInfo, StudentCourseRegistration
from .models import CourseFeedbackDetail, StatewiseDistrict, StateIndia
from .models import EmployerUser, JobProfile, AadharDummy, TrainingCenterJobRole

from .serializers import TrainingCenterCourseSerializer, CustomTestSerializer
from .serializers import CourseInfoSerializer, TrainingCenterSerializer, LoginCheckSerializer
from .serializers import CandidateRegistrationSerializer, AppUserSerializer, JobRoleSerializer
from .serializers import BatchInfoSerializer, StudentCourseRegistrationSerializer
from .serializers import CourseFeedbackDetailSerializer, EmployerUserSerializer
from .serializers import JobProfileSerializer, TrainingCenterJobRoleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

import xlrd
import requests
from textblob import TextBlob


##############################################################
# api/customtest/
class CustomTestList(APIView):

	def get(self, request):

		customtests = CustomTest.objects.all()
		serializer = CustomTestSerializer(customtests, many=True)
		return Response(serializer.data)
##############################################################

# api/trainingcenter/
# Takes training center district as a request parameter
# and returns all the training centers based on the district

class TrainingCenterList(APIView):
	 ## GPS
	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			training_center_district = jsonobject["training_center_district"]
		except:
			training_center_district = request.data["training_center_district"]
		trainingcenters = TrainingCenter.objects.filter(training_center_district=training_center_district)
		serializer = TrainingCenterSerializer(trainingcenters, many=True)
		return Response({'data':serializer.data})

##############################################################

# api/singletrainingcenter
# Takes Center Id as a request parameter and returns the details of the
# training center based on the center id

class SingleTrainingCenter(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		#print(jsonobject)
		center_id = data["center_id"]
		#center_id = request.data["center_id"]
		try:
			trainingcenter = TrainingCenter.objects.get(center_id=center_id)
			serializer = TrainingCenterSerializer(trainingcenter)
			return Response({'data':serializer.data})
		except:
			return Response(False)

##############################################################

# api/candidates/
# get() -- returns the details of all the candidates
# post() -- Takes App user Email as a request parameter
	# and returns the details of the user based on the User Email
	# to check if the "user registrations status" is "True" or "False"

"""
Candidate information Lists and registraion
"""
class CandidateList(APIView):

	def get(self, request):
		candidates = CandidateRegistration.objects.all()
		serializer = CandidateRegistrationSerializer(candidates, many=True)
		return Response({'candidate_list': serializer.data})

	def post(self, request, format=None):
		c_app_user_email = request.data["c_app_user_email"]
		candidate = CandidateRegistration.objects.get(c_app_user_email=c_app_user_email)
		serializer = CandidateRegistrationSerializer(candidate)
		return Response(serializer.data)

class CandidateListBasedOnTrainingCenter(APIView):

	def post(self, request, format=None):
		center_id = request.data["center_id"]
		tc_obj = TrainingCenter.objects.get(center_id=center_id)
		candidate_obj = StudentCourseRegistration.objects.filter(scr_training_center_id=tc_obj)
		serializer = StudentCourseRegistrationSerializer(candidate_obj, many=True)
		return Response({'data':serializer.data})

"""class ReturnCertifiedTraineeList(models.Model):

	def post(self, requests, format=None):

		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data=request.data

		candidate_obj = CandidateRegister.objects.filter(is_certified=True, c_state_ut=data["state"], c_district=data["district"])
		serializer = CandidateRegistrationSerializer(candidate_obj, many=True)
		return Response({'data':serializer.data})
"""
##############################################################

# api/candidates/
# Takes the whole candidate registration credentials as request parameter
# and registers a candidate
# also sets the "user registrations status" by using app user email

class CandidateRegister(APIView):

	def post(self, request, format=None):
		candidatedata = request.data
		c_app_user_email = request.data["c_app_user_email"]
		serializer = CandidateRegistrationSerializer(data=candidatedata)
		if serializer.is_valid():
			app_user_obj = AppUser.objects.get(user_email=c_app_user_email)
			app_user_obj.user_registration_status = True
			app_user_obj.save()
			instance = serializer.save()
			print(True)
			return Response(True)
		return Response(False)

##############################################################

# api/batchinfolist/
# returns all the batch details

class BatchInfoList(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		id = data["batch_id"]
		batchlist = BatchInfo.objects.filter(id=id)
		serializer = BatchInfoSerializer(batchlist, many=True)
		return Response({'data':serializer.data})

##############################################################

# api/batchinfocourse/
# Takes Training Center Id and Course Id as a request parameter
# and returns the batch details based on the parameters

class BatchInfoCourse(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			training_center_id = jsonobject["training_center_id"]
			course_id = jsonobject["course_id"]
		except:
			training_center_id = request.data["training_center_id"]
			course_id = request.data["course_id"]

		courseobj = CourseInfo.objects.get(course_id=course_id)
		center_id = TrainingCenter.objects.get(center_id=training_center_id)
		batchlist = courseobj.batchinfo_set.filter(training_center_id=center_id.id)
		serializer = BatchInfoSerializer(batchlist, many=True)
		return Response({'data':serializer.data})

##############################################################

# api/users/
# get() -- returns the details of all the users
# post() -- Takes all the user registrations credentials as a request parameter
	# and returns "True" if registrations is successful or "False" if Not

"""
	Login Singup credentials - register, login check
"""

class AppUserView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
    	user = AppUser.objects.all()
    	serializer = AppUserSerializer(user, many=True)
    	return Response({'data':serializer.data})

    def post(self, request, format=None):
    	## apparently request from android is coming in bytes form
    	## changed the code .. might have to keep it like this or use try-catch block in future
    	jsonobject = json.loads((request.body).decode("utf-8"))
    	jsonobject1 = json.dumps(jsonobject)
    	print(jsonobject1)
    	print(request.body)
    	jsonobject2 = json.loads(jsonobject1)
    	#print(jsonobject)
    	#jsonobject1 = json.loads(jsonobject)
    	#print(jsonobject1)
    	serializer = AppUserSerializer(data=jsonobject2)
    	if serializer.is_valid():
    		instance = serializer.save()
    		print(serializer.data)
    		print(True)
    		return Response(True, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
	Login Singup credentials - register, login check
	api url = /api/users/
"""
class AppUserView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
    	user = AppUser.objects.all()
    	serializer = AppUserSerializer(user, many=True)
    	return Response({'data':serializer.data})

    def post(self, request, format=None):
    	try:
    		jsonobject = json.loads(request.body)
    		data = jsonobject
    	except:
    		data = request.data
    	serializer = AppUserSerializer(data=data)
    	if serializer.is_valid():
    		instance = serializer.save()
    		print(True)
    		return Response(True, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##############################################################

# api/logincheck/
# Takes User Email and User Password as a request parameter
# and uses it for authentication purpose

class LoginCheck(APIView):

	def post(self, request, format=None):
		jsonobject = json.loads((request.body).decode("utf-8"))
		jsonobject1 = json.dumps(jsonobject)
		jsonobject2 = json.loads(jsonobject1)
		print(request.body)
		print(jsonobject)
		user_email = jsonobject2["user_email"]
		user_password = jsonobject2["user_password"]
		try:
			user = AppUser.objects.get(user_email=user_email)
			if user.user_email==user_email and user.user_password==user_password:
				return Response(True, status=status.HTTP_201_CREATED)
			return Response(False, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response(False, status=status.HTTP_400_BAD_REQUEST)

##############################################################

# api/jobroledata/
# returns all the job roles

"""
JobRole, Course and Batch API's
"""
class JobRoleData(APIView):

	def get(self, request, format=None):
		jobroles = JobRole.objects.all()
		serializer = JobRoleSerializer(jobroles, many=True)
		return Response({'data':serializer.data})
"""
api/jobrolesector/
returns job role based on sector
"""
class JobRoleBasedOnSector(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			sector_skill_council_name = jsonobject["sector_skill_council_name"]
		except:
			sector_skill_council_name = request.data["sector_skill_council_name"]

		job_role_sector = SectorSkillCouncil.objects.get(sector_skill_council_name=sector_skill_council_name)
		job_role_list = job_role_sector.jobrole_set.all()
		serializer = JobRoleSerializer(job_role_list, many=True)
		return Response({'data':serializer.data})
"""
url = api/trainingcenterbasedonjobrole/
"""
class TrainingCenterBasedOnJobRole(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data

		job_role_name = data["job_role_name"]
		job_role_obj = JobRole.objects.get(job_role_name=job_role_name)
		tc_list = TrainingCenterJobRole.objects.filter(job_role_id=job_role_obj)
		serializer = TrainingCenterJobRoleSerializer(tc_list, many=True)
		return Response({'data':serializer.data})
##############################################################

# api/coursedata/
# get() -- returns details of all the courses
# post() -- Takes Job Role name as a request parameter
	# and returns all the course list based on the parameter

class CourseData(APIView):

	def get(self, request, format=None):
		courselist = CourseInfo.objects.all()
		serializer = CourseInfoSerializer(courselist, many=True)
		return Response({'data':serializer.data})

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			jobrolekey = jsonobject["job_role_name"]
		except:
			jobrolekey = request.data["job_role_name"]
		jobroleobj = JobRole.objects.get(job_role_name=jobrolekey)
		courselist = jobroleobj.courseinfo_set.all()
		serializer = CourseInfoSerializer(courselist, many=True)
		return Response({'data':serializer.data})

##############################################################

# api/browsecourse/


##############################################################

# api/fetchtrainingcentercourse/
# Takes Training Center Id as a request parameter
# and returns all the courses provided by

class FetchTrainingCenterCourse(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			training_center_id = jsonobject["training_center_id"]
		except:
			training_center_id = request.data["training_center_id"]
		t_id = TrainingCenter.objects.get(center_id=training_center_id)
		datalist = TrainingCenterCourse.objects.filter(training_center_id=t_id)
		serializer = TrainingCenterCourseSerializer(datalist, many=True)
		return Response({'data':serializer.data})


##############################################################

class StudentCourseList(APIView):

	def get(self, request, format=None):
		studentcourselist = StudentCourseRegistration.objects.all()
		serializer = StudentCourseRegistrationSerializer(studentcourselist, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		try:
			user_email = json.loads(request.body)["user_email"]
		except:
			user_email = request.data["user_email"]
		#training_center_id = request.data["training_center_id"]
		user_obj = AppUser.objects.get(user_email=user_email)
		courselist = user_obj.studentcourseregistration_set.all()
		serializer = StudentCourseRegistrationSerializer(courselist, many=True)
		return Response(serializer.data)

class GetStudentDetails(APIView):

	def post(self, request, format=None):
		"""
			return candidate details if registration status is true
			other wise return false
		"""
		user_email = request.data["user_email"]
		app_user_obj = AppUser.objects.get(user_email=user_email)
		if app_user_obj.user_registration_status is True:
			candidate_obj = CandidateRegistration.objects.get(c_app_user_email=user_email)
			serializer = CandidateRegistrationSerializer(candidate_obj)
			return Response({'data':serializer.data})
		else:
			return Response(False)

class StudentCourseRegistrationForm(APIView):

	def post(self, request, format=None):
		"""
			return true for confirm registration
			otherwise return false
		"""
		data = request.data
		print(data)
		user_email = request.data["user_email"]
		scr_user_id = AppUser.objects.get(user_email=user_email)
		course_id = request.data["course_id"]
		scr_course_id = CourseInfo.objects.get(course_id=course_id)
		training_center_id = request.data["training_center_id"]
		scr_training_center_id = TrainingCenter.objects.get(center_id=training_center_id)
		scr_obj = StudentCourseRegistration.objects.create(scr_user_id=scr_user_id, scr_course_id=scr_course_id, scr_training_center_id=scr_training_center_id)
		return Response({'scr_id':scr_obj.id})

class StudentCompletedCourses(APIView):

	def post(self, request, format=None):
		user_email = request.data["user_email"]
		app_user_obj = AppUser.objects.get(user_email=user_email)
		student_completed_course_list = app_user_obj.studentcourseregistration_set.filter(scr_is_completed=True)
		serializer = StudentCourseRegistrationSerializer(student_completed_course_list, many=True)
		return Response({'data':serializer.data})

class StudentOngoingCourses(APIView):

	def post(self, request, format=None):
		user_email = request.data["user_email"]
		app_user_obj = AppUser.objects.get(user_email=user_email)
		student_ongoing_course_list = app_user_obj.studentcourseregistration_set.filter(scr_is_completed=False)
		serializer = StudentCourseRegistrationSerializer(student_ongoing_course_list, many=True)
		return Response({'data':serializer.data})

class FeedbackStudentCompletedCourses(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		user_email = data["user_email"]
		app_user_obj = AppUser.objects.get(user_email=user_email)
		student_completed_course_list = app_user_obj.studentcourseregistration_set.filter(scr_is_completed=True, scr_has_given_feedback=False)
		serializer = StudentCourseRegistrationSerializer(student_completed_course_list, many=True)
		return Response({'data':serializer.data})

class TrainingCenterFeedback(APIView):

	def get(self, request):
		training_center_id = 'k1'
		cfd_polarity_pos_list = []
		cfd_polarity_neg_list = []
		cfd_training_center_id = TrainingCenter.objects.get(center_id=training_center_id)
		list_feedbacks = CourseFeedbackDetail.objects.filter(cfd_training_center_id=cfd_training_center_id)
		serializer = CourseFeedbackDetailSerializer(list_feedbacks, many=True)
		for item in serializer.data:
			pol = TextBlob(item['cfd_detail']).sentiment.polarity
			if pol >= 0:
				cfd_polarity_pos_list.append(pol)
			else:
				cfd_polarity_neg_list.append(pol)
		total_len = len(cfd_polarity_neg_list) + len(cfd_polarity_pos_list)
		print(total_len)
		pos_percent = (float(len(cfd_polarity_neg_list))/total_len)*100
		neg_percent = (float(len(cfd_polarity_pos_list))/total_len)*100
		return Response({'pos_list':cfd_polarity_pos_list ,'neg_list':cfd_polarity_neg_list})



class CourseFeedback(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			user_email = jsonobject["user_email"]
			training_center_id = jsonobject["training_center_id"]
			course_id = jsonobject["course_id"]
			cfd_subject = jsonobject["subject"]
			cfd_detail = jsonobject["detail"]
			cfd_rating = jsonobject["rating"]
		except:
			user_email = request.data["user_email"]
			training_center_id = request.data["training_center_id"]
			course_id = request.data["course_id"]
			cfd_subject = request.data["subject"]
			cfd_detail = request.data["detail"]
			cfd_rating = request.data["rating"]

		app_user_obj = AppUser.objects.get(user_email=user_email)
		course_obj = CourseInfo.objects.get(course_id=course_id)
		scr_obj = StudentCourseRegistration.objects.get(scr_user_id=app_user_obj, scr_course_id=course_obj)
		scr_obj.scr_has_given_feedback = True
		scr_obj.save()
		training_center_obj = TrainingCenter.objects.get(center_id=training_center_id)
		cfd_obj = CourseFeedbackDetail.objects.create(cfd_user_id=app_user_obj, cfd_training_center_id=training_center_obj, cfd_course_id=course_obj, cfd_subject=cfd_subject, cfd_detail=cfd_detail, cfd_rating=cfd_rating)
		return Response({'id':cfd_obj.id, 'subject':cfd_obj.cfd_subject})

"""
statewise district list
url api/districtlist/
"""
class DistrictList(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			state = jsonobject["state"]
		except:
			state = request.data["state"]
		districtlist = []
		state_obj = StateIndia.objects.get(si_name=state)
		district_all = state_obj.statewisedistrict_set.all()
		print(district_all)
		for item in district_all:
			districtlist.append(item.sd_district_name)
		print(str(districtlist))
		return Response({'district':districtlist})


"""
Employer api's
url api/employer/employerregister
"""
class EmployerRegister(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
		except:
			jsonobject = request.data
		print(jsonobject)
		serializer = EmployerUserSerializer(data=jsonobject)
		if serializer.is_valid() :
			serializer.save()
			print(True)
			return Response(True, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##############################################################

# api/employer/employerlogincheck
# Takes Employer Email and Employer Password as a request parameter
# and uses it for authentication purpose

class EmployerLoginCheck(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			print(jsonobject)
			eu_email = jsonobject["eu_email"]
			eu_password = jsonobject["eu_password"]
		except:
			eu_email = request.data["eu_email"]
			eu_password = request.data["eu_password"]
		try:
			eu_user = EmployerUser.objects.get(eu_email=eu_email)
			if eu_user.eu_email==eu_email and eu_user.eu_password==eu_password:
				return Response(True, status=status.HTTP_201_CREATED)
			return Response("pass error", status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response("exception", status=status.HTTP_400_BAD_REQUEST)

"""
url api/employer/createjob
"""
class CreateJob(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data= request.data
		eu_email = data["eu_email"]
		eu_obj = EmployerUser.objects.get(eu_email=eu_email)
		job_role_name = data["job_role_name"]
		job_role_obj = JobRole.objects.get(job_role_name=job_role_name)
		jp_job_desc = data["jp_job_desc"]
		jp_salary_low = data["jp_salary_low"]
		jp_salary_high = data["jp_salary_high"]
		try:
			job_profile_obj = JobProfile.objects.create(jp_employer_id=eu_obj, jp_job_role_name=job_role_obj, jp_job_desc=jp_job_desc, jp_salary_low=jp_salary_low, jp_salary_high=jp_salary_high)
			return Response(True)
		except:
			return Response("except part")


"""
url api/employer/cetifiedtrainees/
"""
"""class CertifiedTrainees(APIView):

	def post(self, request, format=None):
		try:
			data = json.
"""

""" ####################################################################
AADHAR FETCHING
"""
"""
send otp
"""
class SendOtp(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		ad_aadhar_no = data["ad_aadhar_no"]
		try:
			ad_obj = AadharDummy.objects.get(ad_aadhar_no=ad_aadhar_no)
			ad_mobile_no = ad_obj.ad_mobile_no
			# call method for sending otp
			# store generate otp mapped with aadhar no
			return Response(True)
		except:
			return Response(False)

class FetchAadharDetail(APIView):

	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		is_verified = data["is_verified"]
		ad_aadhar_no = data["ad_aadhar_no"]
		app_user_email = data["c_app_user_email"]
		if is_verified == "true" :
			ad_obj = AadharDummy.objects.get(ad_aadhar_no=ad_aadhar_no)
			candidate_add = CandidateRegistration.objects.create(c_name=ad_obj.ad_fullname, c_email_id=ad_obj.ad_email, c_contact_number=ad_obj.ad_mobile_no, c_gender=ad_obj.ad_gender, c_address=ad_obj.ad_address,c_app_user_email=app_user_email)
			app_user_obj = AppUser.objects.get(user_email=app_user_email)
			app_user_obj.user_registration_status = True
			return Response(True)
		return Response(False)

"""
GPS
"""
class GpsTrainingCenterView(APIView):
	def post(self, request, format=None):
		try:
			jsonobject = json.loads(request.body)
			data = jsonobject
		except:
			data = request.data
		tc_lat = data["tc_lat"]
		tc_lon = data["tc_lon"]
		radius = 5000000
		limit=50000
		radius = float(radius) / 1000.0
		query = """SELECT *, (6367*acos(cos(radians(%2f))*cos(radians(tc_lat))*cos(radians(tc_lon)-radians(%2f))+sin(radians(%2f))*sin(radians(tc_lat)))) AS distance FROM training_center HAVING distance < %2f ORDER BY distance LIMIT 0, %d""" % (float(tc_lat), float(tc_lon), float(tc_lat), radius, limit)
		queryset = TrainingCenter.objects.raw(query)
		serializer = TrainingCenterSerializer(queryset, many=True)
		return Response({'data':serializer.data})

class fetchtrainingcenteronce(APIView):
	def get(self, request, format=None):
		import time
		file = xlrd.open_workbook("/home/vaibhav/Downloads/sheet.xlsx", "rb")
		first_sheet = file.sheet_by_index(0)
		print first_sheet.row_values(0)
		for i in range(5):
			tempdata = first_sheet.row_values(i)

			center_id = tempdata[3]
			try:
				tc_obj = TrainingCenter.objects.get(center_id=center_id)
				return Response(True)
			except:
				complete_address = str(tempdata[3])+',+'+str(tempdata[2]).replace(" ","+")

				print("\n\n"+complete_address)
				url = "https://maps.googleapis.com/maps/api/geocode/json?address="+complete_address+"&key=AIzaSyA9FK6FF-yyq_SZK9NzaItymOYVEH9E2AU"
				response = requests.get(url)
				print(response.text)
				jsonobject = json.loads(response.text)
				result = jsonobject["results"][0]
				lat = result["geometry"]["location"]["lat"]
				lon = result["geometry"]["location"]["lng"]
				print(tempdata[10])
				tc_obj = TrainingCenter.objects.create(center_id=str(tempdata[1]), password="password", training_center_state=str(tempdata[2]), training_center_district=str(tempdata[3]), parliamentary_constituency=str(tempdata[4]), training_partner=str(tempdata[5]), training_center_name=str(tempdata[6]), sector_skill_council=str(tempdata[7]), job_role_name=str(tempdata[8]), qp_code = str(tempdata[9]), level=tempdata[10], no_of_hours=tempdata[13], target_allocated=tempdata[14], center_poc_name=str(tempdata[15]), center_poc_email=str(tempdata[16]), address="temp", tc_lat=lat, tc_lon=lon)
				return Response(True)
				time.sleep(5, verify=True)
			return Response(True)
