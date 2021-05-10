from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('required/', views.required),
    path('profiles/', include('profiles.urls')),
    path('', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)