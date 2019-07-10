from rest_framework import serializers

from .models import ComissionPlan


class ComissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionPlan
        fields = ('id', 'lower_percentage', 'upper_percentage', 'min_value')
