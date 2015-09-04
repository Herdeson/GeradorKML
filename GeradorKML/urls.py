from django.conf.urls import include, url
from django.contrib import admin
from google.views import loginK , logoffK

urlpatterns = [
    # Examples:
    # url(r'^$', 'GeradorKML.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    

    url(r'^$',loginK),
    url(r'^login', loginK , name='login'),
    #url(r'^logoff', logoffK, name='logoff'),
    url(r'^logoff/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='accounts_logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^google/', include('google.urls')),
]
