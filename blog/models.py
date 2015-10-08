from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255 )
    datetime = models.DateTimeField (u'Дата публикации')
    content = models.TextField (max_length = 10000)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class SighUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = False, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.email