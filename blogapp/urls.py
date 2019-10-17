from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
#for using the media file variables
from django.conf import settings
#for static files(css)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#for media files(images)
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
#appending url for static_files(css)
urlpatterns += staticfiles_urlpatterns()
#appending url for media_file(images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
