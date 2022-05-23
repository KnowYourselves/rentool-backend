# django
from django.urls import path

# others libraries
from rest_framework.urlpatterns import format_suffix_patterns

from listings import views

urlpatterns = [
    path("tool_listings/", views.ToolListingList.as_view()),
    path("tool_listings/<int:pk>/", views.ToolListingDetail.as_view()),
    path("reviews/", views.ReviewList.as_view()),
    path("reviews/<int:pk>/", views.ReviewDetail.as_view()),
    path("past_tool_listings/", views.PastToolListingList.as_view()),
    path("past_tool_listings/<int:pk>/", views.PastToolListingDetail.as_view()),
    path("complaints/", views.ListingComplaintList.as_view()),
    path("complaints/<int:pk>/", views.ListingComplaintDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
