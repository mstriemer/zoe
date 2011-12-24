from django.db import models

from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_published = models.DateTimeField(null=True, editable=False)
    date_updated = models.DateTimeField(editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.date_updated = datetime.now()
        super(Post, self).save(*args, **kwargs)
