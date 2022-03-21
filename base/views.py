# others libraries
from rest_framework import views
from rest_framework.response import Response


class PingApiView(views.APIView):
    def get(self, request, format=None):
        return Response("pong")
