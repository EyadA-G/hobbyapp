from rest_framework import serializers
from mainapp.models import Hobbies, Users

class UserSerializer(serializers.ModelSerializer):
    photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    hobbies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Users
        fields = [ 'user', 'name', 'email', 'city', 'photo_url', 'dateOfBirth', 'hobbies' ]
