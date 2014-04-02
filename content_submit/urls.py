from django.conf.urls import patterns, url
from content_submit import views

urlpatterns = patterns('',
	url(r'^$', views.home_page, name='home_page'),
	)