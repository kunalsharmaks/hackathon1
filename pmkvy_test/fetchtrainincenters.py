import xlrd
import requests
import json
from .models import TrainingCenter

file = xlrd.open_workbook("/home/vaibhav/Downloads/sheet.xlsx", "rb")

first_sheet = file.sheet_by_index(0)

print first_sheet.row_values(0)

tempdata = first_sheet.row_values(1)

center_id = tempdata[1]

center_id = int(center_id)

try:
	tc_obj = TrainingCenter.objects.get(center_id=center_id)
except:
	complete_address = str(tempdata[17]).replace(' ','+')
	complete_address = complete_address+',+'+str(tempdata[3])+',+'+str(tempdata[2]).replace(' ','+')
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+complete_address+"&key=AIzaSyA9FK6FF-yyq_SZK9NzaItymOYVEH9E2AU"
	response = requests.get(url)
	jsonobject = json.loads(response.text)
	result = jsonobject["results"][0]
	lat = result["geometry"]["location"]["lat"]
	lon = result["geometry"]["location"]["lng"]
	tc_obj = models.TrainingCenter.objects.create(center_id=int(tempdata[1]), password="password", training_center_state=str(tempdata[2]), training_center_district=str(tempdata[3]), parliamentary_constituency=str(tempdata[4]), training_partner=str(tempdata[5]), training_center_name=str(tempdata[6]), sector_skill_council=str(tempdata[7]), job_role_name=str(tempdata[8]), qp_code = str(tempdata[9]), level=int(tempdata[10]), no_of_hours=int(tempdata[13]), target_allocated=int(tempdata[14]), center_poc_name=str(tempdata[15]), center_poc_email=str(tempdata[16]), address=str(tempdata[17]), tc_lat=lat, tc_lon=lon)



