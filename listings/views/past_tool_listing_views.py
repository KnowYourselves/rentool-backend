# others libraries
from rest_framework import generics

from listings.models import PastToolListing
from listings.serializers import PastToolListingSerializer


class PastToolListingList(generics.ListCreateAPIView):
    queryset = PastToolListing.objects.all()
    serializer_class = PastToolListingSerializer


class PastToolListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastToolListing.objects.all()
    serializer_class = PastToolListingSerializer
