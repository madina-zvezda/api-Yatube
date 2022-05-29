from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts/(?P<id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
