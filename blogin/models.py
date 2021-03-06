from django.db import models

# Create your models here.
class Post(models.Model):
	sno=models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	content=models.CharField(max_length=100)
	author=models.CharField(max_length=50)
	slug=models.CharField(max_length=105)
	timestamp=models.DateTimeField(blank=True)

	def __str__(self):
		return self.title+ " by " +self.author