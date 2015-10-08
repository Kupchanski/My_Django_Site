from django.contrib import admin
from .models import Post, SighUp
from .forms import SighUpForm

class SighUpAdmin (admin.ModelAdmin):
	list_display = ["__str__",'timestamp', "updated"]
	form = SighUpForm
	#class Meta:
	#	model = SighUp

admin.site.register(Post)
admin.site.register(SighUp, SighUpAdmin)