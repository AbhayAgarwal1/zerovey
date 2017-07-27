
from django import forms
from django.contrib.auth.models import User
from zerovey.models import  UserProfile,Blog
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('gender', 'skin_type','hair_type')




class blogForm(forms.ModelForm):

	title = forms.CharField(max_length=128,
		help_text="Please enter the title name.")
	body = forms.CharField(max_length=128,
		help_text="Please enter the title name.")


	class Meta:
		model = Blog
		fields = ('title','body')

