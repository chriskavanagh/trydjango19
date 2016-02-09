from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
#from django.db.models.signals import post_save, pre_save
from autoslug import AutoSlugField



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    #slug = models.SlugField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='title', unique =True)     # Parameters For Auto Slug: http://django-autoslug.readthedocs.org/en/latest/fields.html
    
    def __unicode__(self):
        return self.title
        
    # def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        # super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})    # 'posts.views.post_detail'
        
        

        
## -------------------Signals------------------- ##        
        
# Signal that creates a unique slug for each Post, before the new Post is saved.
# @receiver(pre_save, sender=Post)
# def create_slug(sender, instance, **kwargs):    # pre_save takes only 'sender' & 'instance'.
    # slug = slugify(instance.title)
    # existing_slug = Post.objects.filter(slug=slug).exists()
        
        
# sender: the Post model class
# instance: the Post instance being saved