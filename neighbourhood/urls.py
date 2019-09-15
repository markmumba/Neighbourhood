from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^accounts/profile/', views.profile, name='myProfile'),
    url(r'^create/profile$',views.create_profile, name='new-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^blog',views.blog, name='blog'),
    url(r'^new/blog$',views.new_blog, name='new_blog'),
    url(r'^business',views.business, name='business'),
    url(r'^new/business$',views.new_business, name='new-business'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)