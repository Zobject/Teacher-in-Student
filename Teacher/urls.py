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
# add some url
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'jion/$',views.jion),
    url(r'login/$',views.login),
    url(r'logout/$',views.logout),
#    url(r'loginout/$',views.loginout),
    url(r'create/$',views.create),
    url(r'createteacher/$',views.createteacher),
    url(r'acceptteacher/$',views.acceptteacher),
    url(r'createuser/$',views.createuser),
    url(r'show/$',views.show),
    url(r'profile/$',views.profile),
    url(r'account/$',views.account),
    url(r'emails/$',views.emails),
    url(r'application/$',views.application),
    url(r'reservation/$',views.reservation),
    url(r'password_reset/$',views.password_reset),
    url(r'kemu/$',views.kemu),
    url(r'acceptkecheng/$',views.acceptkecheng),
    url(r'addtime/$',views.addtime),
    url(r'addtime/$',views.accpetaddtime),
    url(r'yue/$',views.yue),
    url(r'teacherlist/$',views.teacherlist),
    url(r'addroom',views.addroom),
   url(r'',views.index),

    # url(r'createkemu/$',views.tianjiakemu),
]



