from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
	pub_date = models.DateTimeField('Date published')
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField (
		unique_for_date='pub_date',
		help_text='Automatically built from the title.'
	)
	tags = TaggableManager()
	enable_comments = models.BooleanField(default=True)
	PUB_STATUS = (
		(0, 'Draft'),
		(1, 'Published'),
	)
	status = models.IntegerField(choices=PUB_STATUS, default=0)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
