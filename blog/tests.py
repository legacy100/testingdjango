from django.test import TestCase
from .models import Post


# Create your tests here.
# To run a test in our terminal
# py manage.py test
# pip install coverage
# coverage run manage.py test
# coverage report
# coverage html
# coverage run --omit='*/env/*' manage.py test
class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
