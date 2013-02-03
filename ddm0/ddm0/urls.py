from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
	
	# Home page
    (r"^$", direct_to_template, {"template": "index.html"}),
	
	(r'^login/$', login),

    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)