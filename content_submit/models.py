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
	title = models.CharField(max_length=254)
	link = models.URLField(max_length=254)
	author = models.CharField(blank=True, max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='content_submit', blank=True)
	category = models.CharField(max_length=220, choices=CATEGORY_CHOICES, default=None)
	publish_date = models.DateField(blank=True, null=True)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


class Submission(models.Model):
	link = models.URLField(max_length=254)
	description = models.TextField()
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)

	def __unicode__(self):
		return self.name

