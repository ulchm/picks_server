from django.conf.urls import include, url
from django.contrib import admin
from schedule.views import GameViewSet, TeamViewSet, SeasonViewSet, LeagueViewSet
from pools.views import PoolViewSet, PickViewSet
from rest_framework import routers
from accounts.views import UserView

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'leagues', LeagueViewSet)
router.register(r'pools', PoolViewSet)
router.register(r'picks', PickViewSet)
router.register(r'accounts', UserView, 'list')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),4
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
