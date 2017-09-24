from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from jchart import Chart
import json
import requests

from api.models import HighAuthCredential
localhost = 'http://localhost:8000'
# Create your views here.
def highAuthLogin(request):
    if request.session.get('ha_email'):
        return HttpResponseRedirect("/highauth/dashboard")
    else:
        return render(request, 'highauth/login.html')

def ha_LoginRedirect(request):
    if request.session.get('ha_email'):
		return HttpResponseRedirect("/highauth/dashboard")
    else:
        ha_obj = HighAuthCredential.objects.get(ha_email='test@gmail.com')
        print("HELlo")
        if ha_obj.ha_password == '1234':
            request.session['ha_email'] = ha_obj.ha_email
            print(True)
            return HttpResponseRedirect("/highauth/dashboard")
        else:
            return HttpResponseRedirect('/highauth/')

def logout(request):
	if request.session.get('ha_email'):
		del request.session['ha_email']
		return HttpResponseRedirect("/highauth/")
	else:
		return HttpResponse("Please Login First")

def ha_dashboard(request):
	# response = requests.get(localhost +'/api/trainingcenterfeedback/')
    if request.session.get('ha_email'):
        center_id = "k1"
        if request.POST:
            center_id = request.POST['center_id']
        url = localhost +'/api/trainingcenterfeedback/'
        data = {
            "training_center_id":center_id
        }
    	response = requests.post(url, data=data)
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
    	return render(request, 'highauth/higherauthority.html', {'training_center_id':center_id, 'data': data, 'pos_percent': pos_percent, 'neg_percent':neg_percent})
    else:
        return HttpResponse("Please Login First")

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
