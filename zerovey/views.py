from django.shortcuts import render
from zerovey.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from zerovey.forms import blogForm
from zerovey.models import Blog


def base(request):
	return render(request, 'zerovey/base.html', {})





def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
# Gather the username and password provided by the user.
# This information is obtained from the login form.
# We use request.POST.get('<variable>') as opposed
# to request.POST['<variable>'], because the
# request.POST.get('<variable>') returns None if the
# value does not exist, while request.POST['<variable>']
# will raise a KeyError exception.
		username = request.POST.get('username')
		password = request.POST.get('password')
# Use Django's machinery to attempt to see if the username/password
# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)
# If we have a User object, the details are correct.
# If None (Python's way of representing the absence of a value), no user
# with matching credentials was found.
		if user:
# Is the account active? It could have been disabled.
			if user.is_active:
# If the account is valid and active, we can log the user in.
# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect(reverse('base'))
			else:
# An inactive account was used - no logging in!
				return HttpResponse("Your Rango account is disabled.")
		else:
# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
# The request is not a HTTP POST, so display the login form.
# This scenario would most likely be a HTTP GET.
	else:
# No context variables to pass to the template system, hence the
# blank dictionary object...
		return render(request, 'zerovey/login.html', {})




def register(request):
# A boolean value for telling the template
# whether the registration was successful.
# Set to False initially. Code changes value to
# True when registration succeeds.
	registered = False
# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
# Attempt to grab information from the raw form information.
# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
# Save the user's form data to the database.
			user = user_form.save()
# Now we hash the password with the set_password method.
# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()
# Now sort out the UserProfile instance.
# Since we need to set the user attribute ourselves,
# we set commit=False. This delays saving the model
# until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user
# Did the user provide a profile picture?
# If so, we need to get it from the input form and
#put it in the UserProfile model.
		
# Now we save the UserProfile model instance.
			profile.save()
# Update our variable to indicate that the template
# registration was successful.
			registered = True
		else:
# Invalid form or forms - mistakes or something else?
# Print problems to the terminal.
			print(user_form.errors, profile_form.errors)
	else:
# Not a HTTP POST, so we render our form using two ModelForm instances.
# These forms will be blank, ready for user input.
		user_form = UserForm()
		profile_form = UserProfileForm()
# Render the template depending on the context.
	return render(request,'zerovey/register.html',{'user_form': user_form,
			'profile_form': profile_form,'registered': registered})

# Create your views here.
def add_blog(request):
	form = blogForm()
	if request.method == 'POST':
		form = blogForm(request.POST)

		if form.is_valid():
			bbb = form.save(commit=False)
			bbb.author = request.user
			bbb.save()
			blogs = Blog.objects.all()

			context_dict = {'categories': blogs}


			return render(request, 'zerovey/blog.html', context_dict)




		else:
			print(form.errors)


	return render(request,'zerovey/add_blog.html',{'form':form})


def blog(request):

	blogs = Blog.objects.all()

	context_dict = {'categories': blogs}


	return render(request, 'zerovey/blog.html', context_dict)


