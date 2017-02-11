from django.conf.urls import url

from . import views

# URL routing within the app
app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^contact/$', views.contact_post, name='contact_post'),
    url(r'^thanks/$', views.thanks_page, name='thanks'),
    url(r'^(?P<post_id>[0-9]+)/$', views.item_detail, name='item_detail'),
]
