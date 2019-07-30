from rest_framework import serializers
from datetime import datetime

from .models import Sales


class SalesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ('id', 'amount', 'seller', 'month', 'comission', 'year')
        extra_kwargs = {
            'comission': {
                'read_only': True,
            },
            'year': {
                'required': False,
                'default': int(datetime.now().strftime('%Y')),
            }
        }

    def create(self, validated_data):

        comission = self.calculate_comission(validated_data)

        return Sales.objects.create(comission=comission, **validated_data)

    def validate_year(self, year):

        if year <= 1980 or year > int(datetime.now().strftime('%Y')):
            raise serializers.ValidationError({'year': ['Ano inválido']})

        return year

    def calculate_comission(self, validated_data):

        amount = validated_data['amount']
        comission_plan = validated_data['seller'].comission_plan

        if(amount >= comission_plan.min_value):
            comission_percentage = comission_plan.upper_percentage
        else:
            comission_percentage = comission_plan.lower_percentage

        comission = comission_percentage/100 * amount

        return comission
