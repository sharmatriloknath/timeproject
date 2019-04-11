from blog.models import Post
from django import template
register=template.Library()


#use of simple_tag
@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()
#useage of inclusion_tag
@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_posts(count=3):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

#useage of assignment_tag
from django.db.models import Count
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
