from django import forms

from .models import SighUp

class ContactForm (forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)

class SighUpForm(forms.ModelForm):
	class Meta:
		model = SighUp
		fields = ['full_name', "email"]
		
	def clean_email(self):
		email =  self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == 'edu':
			raise forms.ValidationError ("Please use valid email")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#ValidationError
		return full_name