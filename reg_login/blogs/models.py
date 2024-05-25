from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_delete
import os
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=250,unique=True,null=False,blank=False)
    summary = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='related_blogs')
    image_small = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return f"{self.title} - {self.posted_by.username}"
    
    class Meta:
        ordering = ('-posted_at',)
    
class CommentModel(models.Model):
    comment = models.CharField(max_length=150)
    image = models.ImageField(null=True,blank=True)
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_on = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='blog_comments')
    comment_at = models.DateTimeField(auto_now=True)
    
@receiver(post_delete, sender=BlogPost)
def delete_media_file_on_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.image_small:
        with open(instance.image_small.path, 'r'):
            pass
        os.remove(instance.image_small.path)

class Query(models.Model):
    query = models.CharField(max_length=250)
    