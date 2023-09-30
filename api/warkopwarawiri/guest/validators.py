from rest_framework import serializers


class PostGuestSubscribeValidation(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    topic = serializers.CharField(required=True, allow_blank=False)