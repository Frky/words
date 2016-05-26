from django.conf.urls import url

from website.views import index, get_last_word
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^get_last_word$', get_last_word, name="get_last_word"),
]
