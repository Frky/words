from django.conf.urls import url

from website.views import index
urlpatterns = [
    url(r'^$', index, name="index"),
]
