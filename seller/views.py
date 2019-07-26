from rest_framework import viewsets, status
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


class RetrieveSellerView(APIView):

    def retrieve(self, request, month):
        sellers = Sales.objects.filter(month=month).order_by('-comission')
        sellers = [{'name': s.id_seller.name,
                    'id': s.id_seller.id,
                    'comission': s.comission} for s in sellers]

        return Response(sellers, status=status.HTTP_200_OK)
        
