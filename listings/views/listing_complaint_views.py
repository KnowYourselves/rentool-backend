# others libraries
from rest_framework import generics

from base.permissions import BlockUnsafeMethods
from listings.models import ListingComplaint
from listings.serializers import ListingComplaintSerializer


class ListingComplaintList(generics.ListCreateAPIView):
    queryset = ListingComplaint.objects.all()
    serializer_class = ListingComplaintSerializer
    permission_classes = (BlockUnsafeMethods,)


class ListingComplaintDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingComplaint.objects.all()
    serializer_class = ListingComplaintSerializer
    permission_classes = (BlockUnsafeMethods,)
