from django.contrib import admin
from django.urls import include, path
from signup.views import signaction, homeaction
from login.views import loginaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction, name='signup'),
    path('login/',loginaction, name='login'),
    path('',homeaction, name='home'),
]
