from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^auth/token/', obtain_jwt_token),
    url(r'^auth/refresh-token/', refresh_jwt_token),
    url(r'^auth/verify-token/', verify_jwt_token),

    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^tweets/', include('tweets.urls', namespace='tweets'))
]
