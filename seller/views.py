from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seller.models import Seller
from seller.serializers import SellerModelSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = SellerModelSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            response = {
                "id": data.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

