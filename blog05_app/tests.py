# blog05_app/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost

# Disables all print() 
if False:
	print("!!!! ALL PRINTING IS DISABLED !!!!    See: tests.py line 10")
	def print(*args, **kw): pass



class BlogTests(TestCase):
	""" """

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username="testuser",
			email="testuser@myemail.com",
			password="secret")

		self.post = BlogPost.objects.create(
			postTitle="My Blog Title",
			postBody="This is the blog body",
			postAuthor=self.user)

	def test_string_form(self):
		""" """
		title = "My Sample Title"
		expStg = f"BlogPost[{title}]"
		post = BlogPost(postTitle=title)
		self.assertEqual(str(post), expStg)

	def test_get_absolute_url(self):
		self.assertEqual(self.post.get_absolute_url(), "/post/1/")

	def test_post_content(self):
		""" """
		self.assertEqual(f"{self.post.postTitle}", "My Blog Title")
		self.assertEqual(f"{self.post.postBody}", "This is the blog body")
		self.assertEqual(f"{self.post.postAuthor}", "testuser")

	def test_post_list_view(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This is the blog body")
		self.assertTemplateUsed(response, "home.html")

	def test_good_post_detail_view(self):
		""" 'good' detail view """
		response = self.client.get("/post/1/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This is the blog body")
		self.assertTemplateUsed(response, "post_detail.html")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ template name: {response.template_name}")

	def test_nosuch_detail(self):
		""" try fetching a non-existent BlogPost obj """
		response = self.client.get("/post/2/")
		self.assertEqual(response.status_code, 404)
		# We got an error before trying to use a template,
		# so no template was accessed
		###print(f"@@@ {response}")
		###print(f"@@@ @@@ template name: {response.template_name}")
		###self.assertTemplateUsed(response, None)
		self.assertFalse(hasattr(response, "template_name"))


	def test_post_create_view(self):
		newTitle = "the new TITLE"
		newBody = "THE BODY!"
		newAuthor = "THE_AUTHOR"
		response = self.client.post(reverse("post_new"),
			{
				"postTitle": newTitle,
				"postBody": newBody,
				"postAuthor": newAuthor,
			})
		#print(f"@@@ @@@ {type(response)}")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ template name: {response.template_name}")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, newTitle)
		self.assertTemplateUsed(response, "post_new.html")


	def test_post_update_view(self):
		""" test /post/NNN/edit/ 
		"""

		objId = "1" #  id = '1'

		# url is str: "/post/1/edit"
		url = reverse("post_edit", args=(objId,))
		#print(f"@@ {url=}")


		newTitle = "TITLE-FROM-test_post_update_view"
		newBody = "BODY~FROM~test_post_update_view"
		argsToPost = {
				"postTitle": newTitle,
				"postBody": newBody,
			}

		response = self.client.post(url, argsToPost)
		self.assertEqual(response.status_code, 302) # 302 == 'Found'

		###self.assertTemplateUsed(response, "post_.......")
		self.assertFalse(hasattr(response, "template_name"))
		# type:  django.http.response.HttpResponseRedirect
		#print(f"@@@ @@@ {type(response)}")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ {str(response)}")
		# The response redirects to the 'show this blog post' URL,
		# namely "/post/1"  -- aka the 'detail' view
		#print(f"@@@ @@@ {response.url}")
		self.assertEqual(response.url, f"/post/{objId}/")


	def test_post_delete_view(self):
		""" test /post/NNN/delete/ 
		"""

		objId = "1" #  id = '1'

		# url is str: "/post/1/edit"
		url = reverse("post_delete", args=(objId,))
		#print(f"@@ {url=}")

		response = self.client.post(url)
		self.assertEqual(response.status_code, 302) # 302 == 'Found'

		###self.assertTemplateUsed(response, "post_.......")
		self.assertFalse(hasattr(response, "template_name"))
		# type:  django.http.response.HttpResponseRedirect
		#print(f"@@@ @@@ {type(response)}")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ {str(response)}")
		# The response redirects to the 'home' URL, namely "/"
		#print(f"@@@ @@@ {response.url}")
		self.assertEqual(response.url, f"/")


		# Another delete attempt should fail

		response = self.client.post(url)
		self.assertEqual(response.status_code, 404) # 404 == 'Not Found'

		###self.assertTemplateUsed(response, "post_.......")
		self.assertFalse(hasattr(response, "template_name"))
		# type:  django.http.response.HttpResponseNotFound
		#print(f"@@@ @@@ {type(response)}")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ {str(response)}")
		# The response has no URL, no redirect
		self.assertFalse(hasattr(response, "url"))



### end ###
