from django.urls import re_path as url
from . import views
'''Define padrões de URL para learning_logs'''
app_name = 'learning_logs'
urlpatterns = [
    # Página inicial https://stackoverflow.com/questions/48271543/typeerror-url-got-an-unexpected-keyword-argument-name-space
    #para cosertar erro do site
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
