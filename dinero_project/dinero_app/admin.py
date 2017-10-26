from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','project_name','project_owner','client','industry',
						'tech_stack','start_date','end_date']
	class Meta:
		model = Projects

admin.site.register(Projects, ProjectsAdmin)
