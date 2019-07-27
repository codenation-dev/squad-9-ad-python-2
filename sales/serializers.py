from rest_framework import serializers

from .models import Sales


class SalesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ('id', 'amount', 'seller', 'month', 'comission')
        extra_kwargs = {
            'comission': {
                'read_only': True,
            }
        }

    def create(self, validated_data):

        if(validated_data['amount'] >=
           validated_data['seller'].comission_plan.min_value):
            comission = validated_data['seller']\
                .comission_plan.upper_percentage/100 * validated_data['amount']
        else:
            comission = validated_data['seller']\
                .comission_plan.lower_percentage/100 * validated_data['amount']

        return Sales.objects.create(comission=comission, **validated_data)
