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
    url(r'^get_num_players', 'voogasalad.views.get_num_players'),
    url(r'^join_game', 'voogasalad.views.join_game'),
    url(r'^post_message', 'voogasalad.views.post_message'),
    url(r'^get_messages/(?P<index>\d+)', 'voogasalad.views.get_messages')
)
