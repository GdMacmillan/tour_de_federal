# urls.py
from django.conf.urls import url
from .views import IndexView, RestarauntDetail

app_name = 'guide'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[a-zA-Z0-9]+)/$', RestarauntDetail.as_view(), name='detail'),
]
