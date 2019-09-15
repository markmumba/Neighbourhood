from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
     url(r'^$',views.index,name='Index'),
    url(r'^accounts/profile/', views.profile, name='myProfile'),
    url(r'^create/profile$',views.create_profile, name='new-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),

]