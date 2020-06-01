# DFB38_07_blog_app/blog05_app/views.py

#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BlogPost


class BlogListView(ListView):
	""" """

	model = BlogPost

	template_name = "home.html"

	# Replace 'object_list' in home page with this more descriptive name
	context_object_name = "all_block_post_objects"


class BlogDetailView(DetailView):
	""" A DetailView expects a primary key -- to obtain the
	details object.
	Can provide either a primary key (aka PK) or a 'slug'.	
	"""

	model = BlogPost

	template_name = "post_detail.html"

	# In the template, you can use either 'object' or 
	# 'blogpost' (lower-cased class name)
	# to access the view.
	# If you provide context_object_name explicitly,
	# you use that instead of 'object'.
	context_object_name = "blog_post_detail_object"


class BlogCreateView(CreateView):
	""" Create a new blog post.
	"""

	model = BlogPost
	template_name = "post_new.html"
	fields = ["postTitle", "postAuthor", "postBody"]

	###context_object_name = "blog_post_create_object"


class BlogUpdateView(UpdateView):
	""" Update an existing blog post """
	model = BlogPost
	template_name = "post_edit.html"
	fields = ["postTitle", "postBody"]
	###context_object_name = "blog_post_edit_object"


class BlogDeleteView(DeleteView):
	""" Delete a blog post """

	model = BlogPost
	template_name = "post_delete.html"
	success_url = reverse_lazy("home")
	# see post_delete.html
	context_object_name = "blog_post_delete_object"


### end ###
