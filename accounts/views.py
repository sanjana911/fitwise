from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts.serializers import CustomerSerializer

# Create your views here.


class CustomerCreateView(CreateAPIView):

    serializer_class = CustomerSerializer

    queryset = User.objects.all()

    def post(self, request):

        form_data = request.data

        serializer_instance = CustomerSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = CustomerSerializer(instance)

            return Response (serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
        



