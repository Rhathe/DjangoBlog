from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "MySite"
    description = "Some ramblings of mine"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-pub_date")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('blog.views',
	url(r'^$', ListView.as_view(
		queryset=Post.objects.all().order_by("-pub_date")[:2],
		template_name="blog.html")),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 
		DetailView.as_view(
			model=Post,
			template_name="post.html")),
	url(r'^archives/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-pub_date"),
		template_name="archives.html")),
	url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
	url(r'^feed/$', BlogFeed()),

)
