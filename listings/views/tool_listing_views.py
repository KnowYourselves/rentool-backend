# others libraries
from rest_framework import generics

from base.permissions import BlockUnsafeMethods
from listings.models import ToolListing
from listings.models.past_tool_listing_models import PastToolListing
from listings.serializers import ToolListingRentSerializer
from listings.serializers import ToolListingSerializer


class ToolListingList(generics.ListCreateAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingSerializer
    permission_classes = (BlockUnsafeMethods,)


class ToolListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingSerializer
    permission_classes = (BlockUnsafeMethods,)


class ToolListingRent(generics.UpdateAPIView, generics.GenericAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingRentSerializer
    permission_classes = (BlockUnsafeMethods,)

    def partial_update(self, request, *args, **kwargs):
        request.data["status"] = ToolListing.Status.RENTED
        response = super().partial_update(request, *args, **kwargs)
        PastToolListing.create_from_listing(self.get_object(), request.user)
        return response
