from django.conf.urls import include, url
from django.contrib import admin
from firstapp import views
from django.conf.urls import include

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name= 'index'),
    url(r'^testadd/',include('firstapp.urls')),
]
