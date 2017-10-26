from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','project_name','project_owner','client','industry',
						'tech_stack','start_date','end_date']
	search_fields = ['project_name']
	list_filter = ['project_name','project_name','project_owner','client','industry',
						'tech_stack']
	class Meta:
		model = Projects

admin.site.register(Projects, ProjectsAdmin)
