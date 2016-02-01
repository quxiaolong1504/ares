from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

# for web site urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'ares.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
]


# for api urls
urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/sms/', include('sms.api.urls', namespace='sms'), name='sms')

]

urlpatterns += format_suffix_patterns(urlpatterns)
