from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voogasalad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_master_json', 'voogasalad.views.get_master_json'),
    url(r'^update_master_json', 'voogasalad.views.update_master_json'),
    url(r'^make_game', 'voogasalad.views.make_game'),
)
