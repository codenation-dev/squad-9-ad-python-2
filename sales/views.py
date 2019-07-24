from rest_framework import viewsets, status
from rest_framework.response import Response
from sales.models import Sales
from sales.serializers import SalesModelSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = SalesModelSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            response = {
                "id": data.id,
                "comission": data.comission
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
