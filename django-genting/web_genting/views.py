from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from web_genting.models import UserProfile, UploadForm, Picture
from django.db.utils import IntegrityError
# Create your views here.
def index_view(request):
	# print 'Get into index'
	
	logInfo = 'None'
	if request.user.is_authenticated(): 
		logInfo = request.user.username
	latest_index = True
	template = loader.get_template('web_genting/index.html')
	context = RequestContext(request, {
		'latest_index': latest_index,
		'name': logInfo,
	})
	print '----------------------'
	print request.user
	print '----------------------'	
	return HttpResponse(template.render(context))

def upload_view(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('web_genting:login'))
	method = request.META['REQUEST_METHOD']
	if method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			pic = Picture(user=request.user, img=form.cleaned_data['img'], text=form.cleaned_data['desc'])
			pic.save()
			return HttpResponseRedirect(reverse('web_genting:index'))	
	return render(request, 'web_genting/upload.html', {})

def signup_view(request):
	method = request.META['REQUEST_METHOD']
	data = {}
	if method == 'POST':
		try:
			user = UserProfile.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
			user.save()
		except Exception, e:
			data['message'] = e.message
		else:
			return HttpResponseRedirect(reverse('web_genting:login'))
	template = loader.get_template('web_genting/signup.html')
	context = RequestContext(request, data)
	return HttpResponse(template.render(context))


def login_view(request):
	logout(request)
	login_msg = ''
	print request.POST
	try: user = authenticate(username=request.POST['username'], password=request.POST['password'])
	#print '============'
	#print user
	#print '============'
	except KeyError:
		login_msg = 'Please provide valid username and password.'
	else: # TODO two step verification here
		if user:
			if user.is_active: 
				print '**************'
				print user
				print '**************'
				login(request, user)

			else: login_msg = 'Trader is deactivated. Contact Support.'
		else: login_msg = 'Authentication Failed. Please try again.' # TODO send notification email
		
		print 'Get user'
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