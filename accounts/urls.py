from django.conf.urls import url
from . import views

app_name ='accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_user, name="signup_user"),
    url(r'^login/$', views.login_user, name="login_user"),
    url(r'^logout/$', views.logout_user, name="logout_user"),
    url(r'^profile/$', views.user_profile, name="user_profile"),
    url(r'^show/(?P<user_id>\d+)/$', views.show_user_profile, name="show_user_profile"),
]

