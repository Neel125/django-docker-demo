from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UserSeralizer(ModelSerializer):
    """Seralizers for the user objects"""
    class Meta:
        model = get_user_model()
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(Serializer):
    """Sertalizer for the user authentication objects"""
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        """Validate and authenticate user"""
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"),
                            username=email,
                            password=password)
        if not user:
            msg = _("Username and Password not matched")
            raise serializers.ValidationError(msg, code="authentication")
        attrs["user"] = user
        return attrs
