from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .util import unique_slug_generator

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=400, null=False)

    slug = models.SlugField(max_length=250, null=True, blank=True)
    blog_content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(slug_generator, sender=BlogPost)