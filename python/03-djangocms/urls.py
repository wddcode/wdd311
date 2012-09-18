from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from wdd.api import *

api = Api(api_name='v1')
api.register(EntryResource())
api.register(RoomResource())
api.register(UserResource())


urlpatterns = patterns('',
                       
    #url(r'^$', 'wdd.views.home', name='home'),
    
    (r'^api/', include(api.urls)),
     
    url(r'^wdd/', include('wdd.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
)
    
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)