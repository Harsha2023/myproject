
from django.contrib import admin
from django.urls import path,include
from todolist_app   import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index,name="index"),
    path('account/',include('users_app.urls')),
    path('todolist/',include('todolist_app.urls')),
    path('about/',todolist_views.about,name="aboutus"),
    path('contact/',todolist_views.contact,name="contactus"),
]
