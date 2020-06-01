# DFB38_07_blog_app/blog05_app/models.py

from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
	""" A post to the blog """

	# NOTE Django adds a primary key field 'id' that contains
	# an auto-incrementing int value, starting at 1.
	# Ref'd as 'id' or 'pk'

	postTitle = models.CharField(max_length=200)
	# many-to-one (many posts per each author)
	# (Each post has only 1 author)
	postAuthor = models.ForeignKey(
					"auth.User",
					on_delete=models.CASCADE)
	postBody = models.TextField()

	def __str__(self):
		return ("%s[%s]" % 
			(self.__class__.__name__,
			 self.postTitle))

	def get_absolute_url(self):
		""" 
		This gets rid of the error from Django:
		  No URL to redirect to. Either provide a url or define a
		  get_absolute_url method on the Model.
		  Because our <form> does not specify which URL to go to
		  after a successful POST.
		"""
		# NOTE that post_detail needs one arg, the PK (primary key)
		# as an int.
		return reverse("post_detail", args=[str(self.id)])



### end ###
