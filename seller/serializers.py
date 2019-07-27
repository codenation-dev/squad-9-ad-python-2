from rest_framework import serializers
from seller.models import Address, Seller


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'complement',
                  'city', 'state', 'country']


class SellerModelSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Seller
        fields = ['id', 'cpf', 'name', 'last_name', 'age',
                  'email', 'phone', 'address', 'comission_plan']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        return Seller.objects.create(address=address, **validated_data)
