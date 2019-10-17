from django.conf.urls import url
from . import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^list/$', views.list, name='list'),
    url(r'^about/$', views.about, name="about"),
    url(r'^announcements/$', views.announcements, name="announcements"),
    url(r'^calenders/$', views.calenders, name="calenders"),
    url(r'^create/$', views.create_blog, name='create_blog'),
    url(r'^confirm-delete/(?P<blog_id>\d+)/$', views.delete_blog_confirmation, name='delete_blog_confirmation'),
    url(r'^delete/(?P<blog_id>\d+)/$', views.delete_blog, name='delete_blog'),
    url(r'^delete-review/(?P<blog_review_id>\d+)/$', views.delete_blog_review, name='delete_blog_review'),
    url(r'^comment/(?P<blog_id>\d+)/$', views.comment_blog, name='comment_blog'),
    url(r'^edit/(?P<blog_id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^(?P<blog_id>\d+)/$', views.blog_detail, name='blog_detail'),
]

