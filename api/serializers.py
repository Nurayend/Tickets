from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('username'),
                                        email=validated_data.get('email'),
                                        password=validated_data.get('password'))
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.save()
        return user

    def update(self, instance, validated_data):
        return instance
