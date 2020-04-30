from rest_framework import routers
from .viewsets import HashtagViewSet, BlogViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('blogs', BlogViewSet, 'blogs')
router.register('hashtags', HashtagViewSet, 'hashtags')

urlpatterns = router.urls
