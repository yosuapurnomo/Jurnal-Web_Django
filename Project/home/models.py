from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=20, null=True)
	body = models.TextField()
	user = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return "{}".format(self.title)
