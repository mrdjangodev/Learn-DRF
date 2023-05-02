from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        # User is being created
        test_user1 = User.objects.create(username="user1", password="qwert1234")
        test_user1.save()
        
        # blog is being created
        test_post1 = Post.objects.create(author=test_user1, title='Blog test title', body="Body is here")
        test_post1.save()
        
    def testBlogContent(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "user1")
        self.assertEqual(title, "Blog test title")
        self.assertEqual(body, "Body is here")
        