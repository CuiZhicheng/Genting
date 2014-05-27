from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'genting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web_genting/', include('web_genting.urls', namespace="web_genting")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
