from django.db import models

class Resource(models.Model):
	LIBRARY = 'Library'
	DOCUMENTATION = 'Documentation'
	TALK = 'Talk'
	TUTORIAL = 'Tutorial'
	BLOG = 'Blog'
	CATEGORY_CHOICES = (
		(LIBRARY, 'Library'),
		(DOCUMENTATION, 'Documentation'),
		(TALK, 'Talk'),
		(TUTORIAL, 'Tutorial'),
		(BLOG, 'Blog'),
	)
	title = models.CharField(max_length=220)
	link = models.URLField(max_length=200)
	author = models.CharField(blank=True)
	description = models.TextField()
	image = models.ImageField(upload_to='content_submit', blank=True)
	category = models.CharField(max_length=220, choices=CATEGORY_CHOICES, default=None)
	publish_date = models.DateField() 

	def __unicode__(self):
		return self.title

