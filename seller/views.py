from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seller.models import Seller
from sales.models import Sales
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


@api_view(['GET'])
def best_sellers(request, month):
    sellers = Sales.objects.filter(month=month).order_by('-amount')
    sellers = [{'name': s.seller.name,
                'id': s.seller.id,
                'amount': s.amount} for s in sellers]

    return Response(sellers, status=status.HTTP_200_OK)
