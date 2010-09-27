from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^feeds/pub/?$', 'backend.views.pub'),
    (r'^feeds/pub/(\d+)/?$', 'backend.views.pub_details'),
    
    (r'^feeds/club/?$', 'backend.views.club'),
    (r'^feeds/club/(\d+)/?$', 'backend.views.club_details'),
    (r'^feeds/club/(\d+)/players/?$', 'backend.views.club_players'),
    
    (r'^feeds/player/?$', 'backend.views.player'),
    (r'^feeds/player/(\d+)/?$', 'backend.views.player_details'),
    (r'^feeds/player/(\d+)/moyenne/?$', 'backend.views.player_moyenne'),
    
    (r'^feeds/match/?$', 'backend.views.match'),
    (r'^feeds/match/(\d+)/?$', 'backend.views.match_details'),
    
    (r'^feeds/agenda/?$', 'backend.views.agenda'),
    (r'^feeds/agenda/(\d+)/?$', 'backend.views.agenda_details'),

    
)
