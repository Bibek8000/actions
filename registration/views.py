from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration
from .serializers import RegistrationSerializer



class RegistrationListAPIView(APIView):
    def get(self,request):

        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
