from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="JigyAasa Admin"
admin.site.site_title="JigyAasa Admin Panel"
admin.site.index_title="Welcome to JigyAasa Admin Panel"


urlpatterns = [
    path("", views.handlelogin,name='handlelogin'),
    path("home", views.home1,name='home'),
    path("about", views.about,name='about'),
    path("contactus", views.contactus,name='contactus'),
    path("signup", views.handlesignup,name='handlesignup'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('profile', views.profile, name="profile"),
    path('post1', views.post1, name="post1"),
    path('comment', views.comment, name="comment"),
    path('technical', views.technical, name="technical"),
    path('askexpert', views.askexpert, name="askexpert"),
    path('general', views.general, name="general"),
    path('search', views.Search, name="Search"),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
