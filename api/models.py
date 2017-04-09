# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

"""
class TableTest(models.Model):
    s_no = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'table_test'
        
"""
class TestTable(models.Model):
    s_no_a = models.IntegerField(default=0)
    name_a = models.CharField(max_length=25) 

    def __str__(self):
        return self.name_a       
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from __future__ import unicode_literals

#from django.db import models

"""
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
"""

class CustomTest(models.Model):
    s_no = models.IntegerField()
    name = models.CharField(max_length=25)

    class Meta:
        managed = True
        db_table = 'custom_test'

    def __str__(self):
        return self.name


class TrainingCenter(models.Model):
    center_id = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=50, blank=False)
    training_center_state = models.CharField(max_length=25)
    training_center_district = models.CharField(max_length=25, blank=True, null=True)
    parliamentary_constituency = models.CharField(max_length=25, blank=True, null=True)
    training_partner = models.CharField(max_length=200, blank=True, null=True)
    training_center_name = models.CharField(max_length=255, blank=True, null=True)
    sector_skill_council = models.CharField(max_length=255, blank=True, null=True)
    job_role_name = models.CharField(max_length=255, blank=True, null=True)
    qp_code = models.CharField(max_length=50)
    level = models.IntegerField(blank=True, null=True)
    no_of_hours = models.IntegerField(blank=True, null=True)
    target_allocated = models.IntegerField(blank=True, null=True)
    center_poc_name = models.CharField(max_length=150, blank=True, null=True)
    center_poc_email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    tc_area = models.CharField(max_length=10, blank=True, null=True)
    tc_no_of_equipments = models.IntegerField(default=0, blank=True)
    tc_no_of_faculties = models.IntegerField(default=0, blank=True)
    tc_grade = models.CharField(max_length=2, blank=True, null=True)
    tc_lat = models.FloatField(null=True, blank=True, default=None)
    tc_lon = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'training_center'   
    
    def __str__(self):
        return self.center_id             

class CandidateRegistration(models.Model):
    c_name = models.CharField(max_length=70)
    c_email_id = models.CharField(unique=True, max_length=255)
    c_alternate_email_id = models.CharField(max_length=255, blank=True, null=True)
    c_contact_number = models.CharField(max_length=12)
    c_alternate_contact_number = models.CharField(max_length=12, blank=True, null=True)
    c_address = models.CharField(max_length=175)
    c_state_ut = models.CharField(max_length=70)
    c_district = models.CharField(max_length=70)
    c_pincode = models.IntegerField(blank=True, default=0)
    c_alternate_address = models.CharField(max_length=175, blank=True)
    c_alternate_state = models.CharField(max_length=70, blank=True)
    c_alternate_district = models.CharField(max_length=70, blank=True)
    c_alternate_pincode = models.IntegerField(blank=True, default=0)
    c_date_of_birth = models.DateField(blank=True, default=timezone.now)
    c_f_name = models.CharField(max_length=70, blank=True)
    c_gender = models.CharField(max_length=12)
    c_category = models.CharField(max_length=12, blank=True)
    c_differently_abled = models.IntegerField(blank=True, null=True)
    c_is_bpl = models.IntegerField(blank=True, default=0)
    c_annual_family_income = models.IntegerField(blank=True, null=True)
    c_educational_qualification = models.CharField(max_length=25, blank=True)
    c_work_experience_months = models.IntegerField(blank=True, null=True)
    c_work_experience_desc = models.CharField(max_length=255, blank=True, null=True)
    c_current_location_state_ut = models.CharField(max_length=25, blank=True)
    c_current_location_district = models.CharField(max_length=25, blank=True)
    c_preferred_training_state_ut = models.CharField(max_length=35, blank=True)
    c_sector = models.CharField(max_length=255, blank=True, null=True)
    c_course = models.CharField(max_length=255, blank=True, null=True)
    c_is_ready_to_relocate = models.IntegerField(blank=True, null=True)
    c_max_fee = models.IntegerField(blank=True, null=True)
    c_is_agree = models.IntegerField(blank=True, null=True)
    c_is_certified = models.BooleanField(default=False, blank=True)
    c_app_user_email = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'candidate_registration'

    def __str__(self):
        return self.c_name

class AppUser(models.Model):
    user_email = models.CharField(max_length=255, unique=True)
    user_password = models.CharField(max_length=128)
    user_last_login = models.DateField(blank=True, null=True)
    user_date_joined = models.DateField()
    user_name = models.CharField(max_length=70)
    user_registration_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class SectorSkillCouncil(models.Model):
    sector_skill_council_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sector_skill_council_name

class JobRole(models.Model):
    job_role_name = models.CharField(max_length=255)
    job_role_sector = models.ForeignKey(SectorSkillCouncil, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_role_name

"""
Course and Batch informations 
"""
class CourseInfo(models.Model):
    course_id = models.CharField(max_length=12, unique=True)
    course_name = models.CharField(max_length=255, default='')
    course_job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    course_sector = models.ForeignKey(SectorSkillCouncil, default='', on_delete=models.CASCADE)
    course_level = models.IntegerField(default=0, blank=True)
    course_no_of_days = models.IntegerField(default=0, blank=True)
    course_minimum_qualification = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return "%s : %s " % (self.course_id, self.course_name)

class BatchInfo(models.Model):
    batch_start_date = models.DateField(default=timezone.now)
    batch_end_date = models.DateField(default=timezone.now)
    course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    training_center_id = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    batch_assessment_date = models.DateField(default=timezone.now)
    batch_no_of_seats = models.IntegerField(default=0)
    batch_last_date_registration = models.DateField(default=timezone.now)

    def __str__(self):
        return "%s : %s : %s" % (self.course_id, self.training_center_id, self.id)

class TrainingCenterCourse(models.Model):
    training_center_id = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE, default=0)
    course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, default='')

    def __str__(self):
        return "%s : %s" % (self.training_center_id, self.course_id)

class TrainingCenterJobRole(models.Model):
    training_center_id = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE, default=0)
    job_role_id = models.ForeignKey(JobRole, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "%s : %s" % (self.training_center_id, self.job_role_id)

class StudentCourseRegistration(models.Model):
    scr_user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=None)
    scr_course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, default=None)
    scr_training_center_id = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE, default='')
    scr_registration_date = models.DateField(default=timezone.now)
    scr_is_completed = models.BooleanField(default=False)
    scr_is_certified = models.BooleanField(default=False)
    scr_has_given_feedback = models.BooleanField(default=False)
    scr_completion_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "%s : %s : %s" % (self.scr_user_id, self.scr_course_id, self.scr_registration_date)

class CourseFeedbackDetail(models.Model):
    cfd_training_center_id = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    cfd_course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    cfd_user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    cfd_subject = models.CharField(max_length=255, blank=True)
    cfd_detail = models.TextField(blank=True)
    cfd_feedback_date = models.DateField(default=timezone.now)
    cfd_rating = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % self.cfd_subject

class StateIndia(models.Model):
    si_name = models.CharField(max_length=255)

    def __str__(self):
        return self.si_name

class StatewiseDistrict(models.Model):
    sd_district_name = models.CharField(max_length=255)
    sd_state_id = models.ForeignKey(StateIndia, on_delete=models.CASCADE)

    def __str__(self):
        return self.sd_district_name

"""
Employer app models

"""
class EmployerUser(models.Model):
    eu_email = models.CharField(max_length=255, unique=True)
    eu_password = models.CharField(max_length=128)
    eu_name = models.CharField(max_length=70)

    def __str__(self):
        return self.eu_name

class JobProfile(models.Model):
    jp_employer_id = models.ForeignKey(EmployerUser, on_delete=models.CASCADE)
    jp_job_role_name = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    jp_job_desc = models.CharField(max_length=255)
    jp_required_starting_date = models.DateField(default=timezone.now)
    jp_required_ending_date = models.DateField(default=timezone.now)
    jp_salary_low = models.IntegerField(default=0)
    jp_salary_high = models.IntegerField(default=0)

    def __str__(self):
        return self.jp_job_role_name

"""
AADHAR DUMMY DATA
"""
class AadharDummy(models.Model):
    ad_aadhar_no = models.CharField(max_length=12, blank=False, unique=True)
    ad_fullname = models.CharField(max_length=255, blank=False)
    ad_mother_name = models.CharField(max_length=255, blank=True)
    ad_year_of_birth = models.IntegerField(default=0, blank=True)
    ad_gender = models.CharField(max_length=10, blank=False)
    ad_address = models.TextField(blank=True)
    ad_state = models.CharField(max_length=35, default='')
    ad_district = models.CharField(max_length=35, default='')
    ad_mobile_no = models.CharField(max_length=12, blank=False, default='')
    ad_email = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.ad_fullname

class CertifiedTraineeList(models.Model):

    certified = models.BooleanField(default=False)
    c_app_user_email = models.CharField(max_length=255, default="", blank=True)
    district = models.CharField(max_length=25, blank=True)
    job_role = models.CharField(max_length=100, blank=True)

    def __str__(self):

        return self.c_app_user_email        