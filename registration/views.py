from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser



class RegistrationListAPIView(APIView):
    parser_classes = [MultiPartParser,FormParser,JSONParser]
    def get(self,request):

        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "registration sucessful",
                "data": serializer.data

            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
