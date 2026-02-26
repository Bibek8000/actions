from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, error_messages={"required":"Name is Required", "blank":"Name cannot be empty"})
    email = serializers.EmailField(error_messages = {"required":"email is required", "blank":"email cannot be empty"})
    password = serializers.CharField(write_only=True, error_messages={"required":"password is required", "blank":"password cannot be empty"})
