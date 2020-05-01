from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def get_fields(self):
	    return [(field.name, field.value_to_string(self)) for field in Task._meta.fields]

	def __str__(self):
		return self.title
