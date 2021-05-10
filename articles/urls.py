from django.urls import path
from . import views
app_name = "articles"
urlpatterns = [
    path('', views.articles_list, name='list'),
    path('create', views.create_post, name='create'),
    path('<url>', views.articles_in, name="articin"),
]
