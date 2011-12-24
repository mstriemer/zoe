"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime

from django.test import TestCase

from posts.models import Post


class PostTest(TestCase):
    def test_unicode(self):
        self.assertEqual(u'My Post', unicode(Post(title='My Post')))

    def test_date_created(self):
        now = datetime.now()
        post = self.make_post()
        assert now < post.date_created

    def test_date_updated(self):
        post = self.make_post()
        initial = post.date_updated
        post.save()
        assert initial < post.date_updated

    def make_post(title='Post', slug='post', **kwargs):
        return Post.objects.create(title=title, slug=slug, **kwargs)
