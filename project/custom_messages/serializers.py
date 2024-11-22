from rest_framework import serializers

from .models import Message
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    shamsi_date = serializers.SerializerMethodField()

    # def get_sender(self, obj):
    #     print("context in get_sender:", self.context)
    #     full_sender_info = self.context.get('full_sender_info', False)
    #     if full_sender_info:
    #         return UserSerializer(object.sender).data
    #     else:
    #         return {'username': obj.sender.username}


    def get_shamsi_date(self, obj):
        return str(obj.shamsi_date)

    # def to_representation(self, instance):
    #     print("custom to_representation called")
    #     data = super().to_representation(instance)
    #     print("Serialized Data", data)
    #     return data


    class Meta:
        model = Message
        fields = ['id', 'text', 'sender', 'shamsi_date', 'is_approved']
        extra_kwargs = {'sender': {'required': False}}
