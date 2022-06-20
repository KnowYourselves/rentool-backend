# others libraries
from rest_framework import generics

from base.permissions import BlockUnsafeMethods
from listings.models import ToolListing
from listings.models.past_tool_listing_models import PastToolListing
from listings.serializers import PastToolListingSerializer
from listings.serializers import ToolListingRentSerializer
from listings.serializers import ToolListingSerializer
from listings.serializers import ToolListingUnrentSerializer


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


class ToolListingUnrent(generics.UpdateAPIView, generics.GenericAPIView):
    queryset = ToolListing.objects.all()
    serializer_class = ToolListingUnrentSerializer
    permission_classes = (BlockUnsafeMethods,)

    def partial_update(self, request, *args, **kwargs):
        request.data["status"] = ToolListing.Status.PUBLISHED
        response = super().partial_update(request, *args, **kwargs)
        return response


class MyPublishedToolListingList(generics.ListAPIView):
    serializer_class = ToolListingSerializer
    permission_classes = (BlockUnsafeMethods,)

    def get_queryset(self):
        return ToolListing.objects.filter(publisher=self.request.user)


class MyRentedToolListingList(generics.ListAPIView):
    serializer_class = PastToolListingSerializer
    permission_classes = (BlockUnsafeMethods,)

    def get_queryset(self):
        return PastToolListing.objects.filter(listing__publisher=self.request.user)

class MyRentalsList(generics.ListAPIView):
    serializer_class = PastToolListingSerializer
    permission_classes = (BlockUnsafeMethods,)

    def get_queryset(self):
        return PastToolListing.objects.filter(renter=self.request.user)
