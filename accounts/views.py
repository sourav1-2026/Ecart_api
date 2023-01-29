from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserRegisterSerializer,LoginSerializer
from rest_framework import status

class UserRegister(APIView):

    def get(self,request):
        return Response({
            "msg":"data get"
        })

    def post(self,request):
        try:
            data=request.data
            serializer=UserRegisterSerializer(data=data)
            if  serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            print("post called1")
            if serializer.is_valid():
                print("post called")
                response=serializer.get_tokens_for_user(serializer.data)
                print("post called 2")
                return Response(response, status=status.HTTP_200_OK)
            return Response({'message':'not able to generate the token'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong to connect'
            },status=status.HTTP_400_BAD_REQUEST)
