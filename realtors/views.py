from django.db.models import query
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer

class RealtorListView(ListAPIView) :
    permissions_classes = (permissions.AllowAny)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None


class RealtorView(RetrieveAPIView) : 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


class TopSellerView(ListAPIView):
    permissions_classes = (permissions.AllowAny)
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None