from django.db import models
from django.utils import timezone

# this is how you instantiate a class in Django
class Post(models.Model):
	# foreignkey is part of the relational side of SQLite
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
