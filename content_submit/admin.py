from django.contrib import admin

from content_submit.models import Resource

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
	date_hierarchy = 'publish_date'

	list_display = ('title', 'author', 'category', 'publish_date', 'active')

	list_filter = ('category',)

	search_fields = ('title', 'author', )


admin.site.register(Resource, ResourceAdmin)