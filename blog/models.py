from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField(blank=False)
    image = models.ImageField(default='default.png', blank = True)
    author = models.ForeignKey(User, default=None, on_delete='cascade')
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

    def get_link(self):
        return self.id

    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50]+' ...'
        else:
            return self.body

    def img_file_name(self):
        return self.image.path


class Blog_reviews(models.Model):
    blog = models.ForeignKey(Blog, default=None,on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(User, default=None, on_delete='cascade')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog_reviews'
        verbose_name_plural = 'Blog_reviews'

    def __str__(self):
        return self.blog.title
