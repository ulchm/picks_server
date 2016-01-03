from pools.models import Pool, Pick
from schedule.models import Season, Game
from .serializers import PoolSerializer, PickSerializer
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from django.utils import timezone


class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


class PickViewSet(viewsets.ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer


def pools(request):
    return render(request, "pools.html")


def add_pool(request):
    name = request.POST.get('name')
    type = request.POST.get('server_visibility')
    season = Season.objects.get(is_active=True)
    #TODO: Make the pool, redirect to a workflow page to invite friends etc.
    return HttpResponseRedirect('/pools/')


def picks(request):
    games = Game.objects.filter(starts_at__gte=timezone.now())
    return render(request, "picks.html", {'games': games})
