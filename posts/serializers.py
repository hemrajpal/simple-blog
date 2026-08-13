from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content"]
        read_only_fields = ["id", "author"]