from rest_framework import serializers
from foodfit.models import Foodlog

class FoodlogSerializer(serializers.ModelSerializer):

    class Meta:

        model = Foodlog

        fields = "__all__"

        read_only_fields =["id"]