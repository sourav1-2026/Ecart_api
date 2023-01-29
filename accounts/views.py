from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserRegisterSerializer
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
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
