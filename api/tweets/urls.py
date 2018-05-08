from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import TweetViewSet

router = DefaultRouter()
router.register(r'tweets', TweetViewSet, base_name='tweets')

urlpatterns = router.urls
