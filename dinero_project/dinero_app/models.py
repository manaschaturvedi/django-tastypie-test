from __future__ import unicode_literals
from django.db import models


class Projects(models.Model):
	project_name = models.CharField(max_length=255)
	project_owner = models.CharField(max_length=255)
	client_name = models.CharField(max_length=255)
	industry = models.CharField(max_length=255)
	tech_stack = models.CharField(max_length=255)
	team_size = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __unicode__(self):

		return self.project_name + ' - ' + self.client_name
