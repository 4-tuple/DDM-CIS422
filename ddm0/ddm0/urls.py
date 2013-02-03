from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	# Home page
    (r"^$", direct_to_template, {"template": "index.html"}),
    
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)