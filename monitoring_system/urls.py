from django.conf.urls import url
from django.views.generic import TemplateView
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#         url(r'^$', views.resource, name='resource'),
#         url(r'^$', views.cpu, name='cpu_query'),
# ]


urlpatterns = [
    url(r'^api/resource/$', views.resource_list),
    url(r'^api/cpu/$', views.cpu_day_list),
    url(r'^api/cpu/detail$', views.cpu_day_detail),
    url(r'^api/cpu/period$', views.cpu_period),
    url(r'^api/cpu/coreday$', views.total_core_per_day),
    url(r'^period$', TemplateView.as_view(template_name = 'monitoring_system/period.html')),
    url(r'^day$', TemplateView.as_view(template_name = 'monitoring_system/day.html')),
    url(r'^$', TemplateView.as_view(template_name = 'monitoring_system/filter.html'))
]

urlpatterns = format_suffix_patterns(urlpatterns)