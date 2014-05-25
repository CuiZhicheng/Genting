# URLconf
from django.conf.urls import patterns, url

from web_genting import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'genting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD
    url(r'^$', views.index_view, name='index'),
    url(r'^signup$', views.signup_view, name='signup'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
=======
    url(r'^$', views.index, name='index'),
>>>>>>> f5fb75f4c6f15bba916aae9b29706c8d2dc11ec8
)