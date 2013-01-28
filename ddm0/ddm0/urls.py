from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	# Home page
    (r"^$", direct_to_template, {"template": "index.html"}),
	
	# Login / Logout - http://neverfear.org/blog/view/97/User_Authentication_With_Django
	url(r'^login/$', 'django.contrib.auth.views.login'),
	# url(r'^logout/$', logout_page),



    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)