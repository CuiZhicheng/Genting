<<<<<<< HEAD
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from web_genting.models import UserProfile
# Create your views here.
def index_view(request):
	# print 'Get into index'
=======
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
>>>>>>> f5fb75f4c6f15bba916aae9b29706c8d2dc11ec8
	latest_index = True
	template = loader.get_template('web_genting/index.html')
	context = RequestContext(request, {
		'latest_index': latest_index,
	})
<<<<<<< HEAD
	#print request.user
	return HttpResponse(template.render(context))


def signup_view(request):
	method = request.META['REQUEST_METHOD']
	data = {}
	if method == 'POST':
		try:
			u = UserProfile(email=request.POST['email'], date_of_birth=request.POST['date_of_birth'], password=request.POST['password'])
			u.save()
		except KeyError:
			data['message'] = str(e)
		else:
			return HttpResponseRedirect(reverse('web_genting:login'))
	template = loader.get_template('web_genting/signup.html')
	context = RequestContext(request, data)
	return HttpResponse(template.render(context))


def login_view(request):
	login_msg = ''
	try: user = authenticate(email=request.POST['email'], password=request.POST['password'])
	except KeyError:
		login_msg = 'Please provide valid username and password.'
	else: # TODO two step verification here
		if user:
			if user.is_active: 
				login(request, user)

			else: login_msg = 'Trader is deactivated. Contact Support.'
		else: login_msg = 'Authentication Failed. Please try again.' # TODO send notification email
		
		# print 'Get user'
		return HttpResponseRedirect(reverse('web_genting:index'))

	# print 'Prepare to get user'	
	request.session['login_msg'] = login_msg
	
	template = loader.get_template('web_genting/login.html')
	context = RequestContext(request, {
		'login_msg': login_msg,
	})
	#print request.COOKIES
	return HttpResponse(template.render(context))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('web_genting:index'))	
=======
	return HttpResponse(template.render(context))
>>>>>>> f5fb75f4c6f15bba916aae9b29706c8d2dc11ec8
