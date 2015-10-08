from django.conf.urls import  include, url
from blog.views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
]