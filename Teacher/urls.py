"""Teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from Test import views
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'jion/$',views.jion),
    url(r'login/$',views.login),
    url(r'create/$',views.create),
    url(r'createteacher/$',views.createteacher),
    url(r'acceptteacher/$',views.acceptteacher),
    url(r'createuser/$',views.createuser),
    url(r'show/$',views.show),
    url(r'kemu/$',views.kemu),
    url(r'acceptkecheng/$',views.acceptkecheng),
    url(r'',views.index)
    # url(r'createkemu/$',views.tianjiakemu),
]



