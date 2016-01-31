from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})    # 'posts.views.post_detail'