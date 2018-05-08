from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, base_name='profiles')

urlpatterns = router.urls
