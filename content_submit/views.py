from django.shortcuts import render
from django.core.mail import send_mail
from content_submit.models import Resource

# Create your views here.
def home_page(request):
	library_resources = Resource.objects.filter(category='Library')
	doc_resources = Resource.objects.filter(category='Documentation')
	talk_resources = Resource.objects.filter(category='Talk')
	tutorial_resources = Resource.objects.filter(category='Tutorial')
	blog_resources = Resource.objects.filter(category='Blog')
	form = request.POST
	link = form.get('link', default=None)
	name = form.get('name', default=None)
	email = form.get('email', default=None)
	description = form.get('description', default=None)

	if request.POST:
		form = request.POST
		send_mail(
			'Asyncio Submission', 
			'%s %s %s' % (name, email, description), 
			'link', 
			['amber.grimaldi@gmail.com']
		)
		if request.is_ajax():
			print "the message should be sent"

	context = {
		'library_resources': library_resources,
		'doc_resources': doc_resources,
		'talk_resources': talk_resources,
		'tutorial_resources': tutorial_resources,
		'blog_resources': blog_resources,
	}

	return render(request, 'content_submit/home_page.html', context)
