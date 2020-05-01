from django.db import models


class blog_model(models.Model):
	title = models.CharField(max_length = 500)
	post = models.TextField()
	image = models.ImageField( upload_to = 'Images/' )
	file_link = models.CharField(max_length=200)
	pub_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	slug = models.SlugField(max_length=500)
	# comments = models.CharField(max_length = 1000)
	# cmt_name = models.CharField(max_length = 200)


	def __str__ (self):
		return self.title

	def prev(self):
		return self.post[: 100] 
# Create your models here.
