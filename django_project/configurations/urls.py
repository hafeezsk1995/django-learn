"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('blue/', include('blue.urls')),
    path('quickstart/', include('quickstart.urls')),
    path('register',user_views.register, name='register'),
    # (This is for finaceeper testings only)
    # url(r'^get_records/$',get_records),
    # url(r'^get_b_emi/$',check_borrower_emi),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
