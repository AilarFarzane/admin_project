from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class UserList(APIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def create_user_from_message(self, phone_number):
        user = CustomUser.objects.get_or_create(phone_number=phone_number)
        return user


