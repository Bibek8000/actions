from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Registration



class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, error_messages={"required":"Name is Required", "blank":"Name cannot be empty"})
    email = serializers.EmailField(error_messages = {"required":"email is required", "blank":"email cannot be empty"})
    password = serializers.CharField(write_only=True, error_messages={"required":"password is required", "blank":"password cannot be empty"})
    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError('password must be at least 8 characters long')
        return value    
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Registration.objects.create(**validated_data)

       
            

