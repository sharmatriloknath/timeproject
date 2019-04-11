from django.db import models
from django.contrib.auth.models import User #Import because we need User Model
from django.utils import timezone #import because we need timezone
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
# Create your models here.

#Fields assoiated with post
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()

    #published posts should display in descending order of date ,latest one should come first
    class Meta:
        ordering=('-publish',)

    #if we need title for that purpose we create it
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comments(models.Model):
    post=models.ForeignKey(Post,related_name='comments')
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'commented by{} on {}'.format(self.name,self.post)
