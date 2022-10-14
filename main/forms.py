from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog
from django.forms import ModelForm, TextInput, Textarea, ImageField
# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class BlogForm(ModelForm):

	class Meta:
		model = Blog
		fields = ['title','description','image']
		queryset = Blog.objects.all()
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Description'}))