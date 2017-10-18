"""RestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
# from Push import views


urlpatterns = [
    url(r'^jet/',include('jet.urls','jet')),
    url(r'^jet/dashboard/',include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/doc/',include('swaggerdoc.urls')),
    url(r'^api/v1/push/',include('Push.urls')),
    url(r'^api/v1/test/',include('Test.urls')),
    url(r'^api/v1/notify/',include('Notify.urls')),
    url(r'^api/v1/news/',include('News.urls')),
    url(r'^api/v1/course/',include('Course.urls')),
    url(r'^webhook/',include('Webhook.urls')),
   
]
