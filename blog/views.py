from blog.models import Post 
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import SighUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SighUp



def home(request):
	title ='Войти как гость'
	form = SighUpForm(request.POST or None)
	context = {
	"title": title,
	'form': form
	}
	
	if form.is_valid():
		#form.save()
		instance = form.save(commit = False )
		full_name = form.cleaned_data.get ("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": 'Thank You'
		}

	# if request.user.is_authenticated() and request.user.is_staff:
	# 	#print(SighUp.objects.all())
	# 	queryset = SighUp.objects.all().order_by('-timestamp').filter(full_name__icontains ='Kup9')
	# 	context = {
	# 	 'queryset': queryset
	# 	}

	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Me'
	form = ContactForm (request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print (key)
		# 	print (form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print (email, message, full_name)
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'kirich_s4@mail.ru' ]
		contact_message = """
		%s: %s via %s
		""" % (form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, 
			contact_message,
			from_email, 
			to_email, 
			fail_silently = False)


	context = {
		'form': form,
		'title':title
	}

	if form.is_valid():
		#form.save()
		context = {
			"title": 'Thank You, we will answer you ASAP'
		}

	return render(request, "forms.html", context)


















