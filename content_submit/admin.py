from django.contrib import admin

from content_submit.models import Resource

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
	date_hierarchy = 'publish_date'

	list_display = ('title', 'category', 'publish_date')

admin.site.register(Resource, ResourceAdmin)