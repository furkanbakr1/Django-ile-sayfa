"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from article import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),   #name = index redirectde direkt index yazarak bağlantılı olduğu urlye gider.
    path('about/', views.about, name = "about"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('iletisim/',views.iletisim,name = "iletisim"),
    path('kisiler/',views.kisiler,name = "kisiler"),
    path('upload/', views.upload_image, name='upload_image'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)