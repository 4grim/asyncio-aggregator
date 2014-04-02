from django.shortcuts import render
from content_submit.models import Resource

# Create your views here.
def home_page(request):
	library_resources = Resource.objects.filter(category='Library')
	doc_resources = Resource.objects.filter(category='Documentation')
	talk_resources = Resource.objects.filter(category='Talk')
	tutorial_resources = Resource.objects.filter(category='Tutorial')
	blog_resources = Resource.objects.filter(category='Blog')

	context = {
		'library_resources': library_resources,
		'doc_resources': doc_resources,
		'talk_resources': talk_resources,
		'tutorial_resources': tutorial_resources,
		'blog_resources': blog_resources,
	}

	return render(request, 'content_submit/home_page.html', context)
