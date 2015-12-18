from django.conf.urls import url
from django.views.generic import TemplateView
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/cpu/main$', views.main),
    url(r'^$', TemplateView.as_view(template_name = 'monitoring_system/main.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)