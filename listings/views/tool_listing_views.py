# others libraries
from rest_framework import generics

from listings.models import ToolListing
from listings.serializers import ToolListingSerializer


class ToolListingList(generics.ListCreateAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingSerializer


class ToolListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingSerializer
