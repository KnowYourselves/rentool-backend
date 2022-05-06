# others libraries
from rest_framework import generics

from listings.models import ListingComplaint
from listings.serializers import ListingComplaintSerializer


class ListingComplaintList(generics.ListCreateAPIView):
    queryset = ListingComplaint.objects.all()
    serializer_class = ListingComplaintSerializer


class ListingComplaintDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingComplaint.objects.all()
    serializer_class = ListingComplaintSerializer
