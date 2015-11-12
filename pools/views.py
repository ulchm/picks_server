from .models import Pool, Pick
from .serializers import PoolSerializer, PickSerializer
from rest_framework import viewsets


class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


class PickViewSet(viewsets.ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer