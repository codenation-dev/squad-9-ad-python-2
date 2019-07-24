from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import ComissionPlanSerializer
from .models import ComissionPlan

# Create your views here.


class ComissionViewSet(viewsets.ModelViewSet):
    queryset = ComissionPlan.objects.all()
    serializer_class = ComissionPlanSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new comission plan
        """
        serializer = ComissionPlanSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            response = {
                "id": data.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
