from django.conf.urls import url
from zerovey import views

urlpatterns = [

	url(r'^register/$',views.register,name='register'),
	url(r'^login/$', views.user_login, name='login'), 
	url(r'^base/$', views.base, name='base'),
	url(r'^addblog/$', views.add_blog, name='add_blog'),
	url(r'^blog/$', views.blog, name='blog'),

	# New pattern!
]