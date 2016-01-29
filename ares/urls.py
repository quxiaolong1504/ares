from django.conf.urls import include, url
from django.contrib import admin

# for web site urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'ares.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


# for api urls
urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/sms/', include('sms.api.urls'))

]
