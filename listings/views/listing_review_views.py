# others libraries
from rest_framework import generics

from base.permissions import BlockUnsafeMethods
from listings.models import Review
from listings.serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (BlockUnsafeMethods,)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (BlockUnsafeMethods,)
