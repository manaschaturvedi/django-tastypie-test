from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Projects


class ProjectsResource(ModelResource):
    class Meta:
        queryset = Projects.objects.all()
        resource_name = 'project'
        filtering = {
        				'project_name': ALL,
        				'industry': ALL,
        				'client_name': ALL,
        				'project_owner': ALL,
        				'tech_stack': ALL,
        				'team_size': ('gt','gte','lt','lte','exact'),
        			}
        allowed_methods = ['get']