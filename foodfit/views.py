from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework  import authentication, permissions

from foodfit.models import Foodlog
from foodfit.serializers import FoodlogSerializer

# Create your views here.

class FoodlogListCreateView(ListAPIView,CreateAPIView):

    serializer_class = FoodlogSerializer

    queryset = Foodlog.objects.all()

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes =[permissions.IsAuthenticated]


    def post(self,request):

        form_data = request.data

        serializer_instance = FoodlogSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer_instance.errors, status= status.HTTP_400_BAD_REQUEST)


class FoodlogRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class = FoodlogSerializer

    queryset = Foodlog.objects.all()

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes =[permissions.IsAuthenticated]


    def put(self,request, pk = None):

        form_data = request.data

        instance = get_object_or_404(Foodlog, id = pk)
        
        serializer_instance = FoodlogSerializer(data = form_data, instance = instance)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
        
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        
        else:
        
            return Response(serializer_instance.errors, status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk = None):

        instance = get_object_or_404(Foodlog, id = pk)

        instance.delete()

        return Response({"message":"deleted.."}, status=status.HTTP_200_OK)



    


        




    