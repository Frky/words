from django.conf.urls import url

from website.views import index, get_last_word, ajax_words
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^get_last_word$', get_last_word, name="get_last_word"),
    url(r'^ajax_words$', ajax_words, name="ajax_words"),
]
