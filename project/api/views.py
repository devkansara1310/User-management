from api.serializers import  RegistrationSerializer, LoginSerializers
from api.models import SystemUser
from api.api_schema import (RegistrationSchema,UpdateUserProfileSchema,LoginSchema,LogoutSchema, UsersSchema)
from django.contrib.auth.models import update_last_login
from django.contrib.auth import logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UserRegistrstion(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    @swagger_auto_schema(**RegistrationSchema.auto_schema)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"code":"1", "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"code":"0", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    @swagger_auto_schema(**LoginSchema.auto_schema)
    def post(self, request):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"code": "1", "token": token.key})

class Logout(APIView):
    @swagger_auto_schema(**LogoutSchema.auto_schema)
    def post(self, request):
        if not self.request.user.is_authenticated:
            return Response({"code":"0", "msg":"You are not logged in."})
        print("self.request.user.", self.request.user)
        request.user.auth_token.delete()
        logout(request)
        return Response('User Logged out successfully')


class UpdateUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(**UpdateUserProfileSchema.auto_schema)
    def post(self, request,pk=None, *args, **kwargs):
        try:
            result = SystemUser.objects.get(id=pk)
            if not self.request.user.is_staff and pk != self.request.user.id:
                return Response({"code":"0", "msg":"You don't have access to modify."})
        except:
            return Response({'code': '0', "msg":"User isn't exist."}, status=200)
        serializer = RegistrationSerializer(result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"code":"1", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"code":"0", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfiles(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(**UsersSchema.auto_schema)
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Response({"code":"0", "msg":"You don't have access to view."})
        if self.request.user.is_staff:
            result = SystemUser.objects.all()
            serializer = RegistrationSerializer(result, many=True)
            return serializer.data
        else:
            return Response({"code":"0", "msg":"Only staff memvber has access to view."})


