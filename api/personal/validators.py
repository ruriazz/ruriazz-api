from rest_framework import serializers


class PostContactJsonValidation(serializers.Serializer):
    sender_name = serializers.CharField(required=True, allow_blank=False)
    sender_email = serializers.EmailField(required=True)
    message = serializers.CharField(required=True, allow_blank=False)