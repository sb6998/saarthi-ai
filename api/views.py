from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import apiSerializer
from .models import api

class apiViewSet(APIView):
    def post(self, request):
        serializer = apiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status_code":status.HTTP_201_CREATED,"status": "success","data":request.data})
        else:
            return Response({"status_code":status.HTTP_400_BAD_REQUEST,"status": "error","data":request.data})
    
    def get(self, request, id = None):
        if id:
            try:
                item = api.objects.get(id=id)
                serializer = apiSerializer(item)
                return Response({"status_code": status.HTTP_200_OK, "status":"success", "data": serializer.data})
            except Exception as e:
                return Response({"status_code": status.HTTP_200_OK, "status":"success", "data": []})

        try:
            items = api.objects.all()
            serializer = apiSerializer(items, many=True)
            return Response({"status_code": status.HTTP_200_OK, "status":"success", "data": serializer.data})
        except Exception as e:
            return Response({"status_code": status.HTTP_200_OK, "status":"success", "data": []})
    
    def delete(self, request, id=None):
        item = get_object_or_404(api, id=id)
        name = item.name
        item.delete()
        return Response({"status_code": status.HTTP_200_OK, "status":"success","message":"The book {} was deleted successfully".format(name), "data":[]})