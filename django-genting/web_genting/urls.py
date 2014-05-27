# URLconf
from django.conf.urls import patterns, url

from web_genting import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'genting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index_view, name='index'),
    url(r'^signup$', views.signup_view, name='signup'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^upload$', views.upload_view, name='upload')
)