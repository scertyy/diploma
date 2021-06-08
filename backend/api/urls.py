from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from backend.api.board.views import BoardViewSet, TaskViewSet, CommentViewSet
from backend.api.profile.views import RegisterApi, ProfileViewSet
from backend.api.team.views import TeamViewSet, ProjectViewSet

router = routers.DefaultRouter()
# Profile
router.register('profile', ProfileViewSet)
# Team
router.register('team', TeamViewSet)
router.register('project', ProjectViewSet)
# Board
router.register('board', BoardViewSet)
router.register('task', TaskViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterApi.as_view())
]
