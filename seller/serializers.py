from rest_framework import serializers

from seller.models import Address, Seller
from comission.models import ComissionPlan

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'complement', 'city', 'state', 'country']

class SellerModelSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    comission =  serializers.PrimaryKeyRelatedField(queryset=ComissionPlan.objects.all())
    
    class Meta:
        model = Seller
        fields = ['id', 'cpf', 'name', 'last_name', 'age', 'email', 'phone', 'address', 'comission']
    
    def create(self, validated_data):
        address_data = validated_data.pop ('address')
        address = Address.objects.create(**address_data)

        return Seller.objects.create(address=address, **validated_data)

         


