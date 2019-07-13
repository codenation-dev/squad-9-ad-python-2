from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ComissionPlanSerializer

# Create your views here.


@api_view(['POST'])
def create_comission_plan(request):
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
