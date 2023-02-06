from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import *
import json
from django.http import JsonResponse

# authentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Throttling
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class CategoryView (viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]

    def list(self,request):
        try:
           
            key=request.build_absolute_uri()
            value = cache.get(key)
            #cache.delete(request.build_absolute_uri())
            # print(value)
            # print(1)
            if value is not None:
                print("cached")
                return JsonResponse(json.loads(value), safe=False)
            CatObj=Category.objects.all()
            serializer=CategorySerializer(CatObj,many=True)
            response=Response(serializer.data)
            # print(serializer)
            # print(type(serializer))
            cache.set(key, json.dumps(serializer.data), timeout=60)
            return response
        except:
             return Response({"msg":"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        try:
            id=pk
            if id is not None:
                key=request.build_absolute_uri()
                value = cache.get(key)
                if value is not None:
                    print("cached")
                    return JsonResponse(json.loads(value), safe=False)
                Catobj=Category.objects.get(pk=id)
                serializer=CategorySerializer(Catobj)
                response = Response(serializer.data)
                print("database")
                cache.set(key, json.dumps(serializer.data), timeout=60)
                return response
            return response({'msg':"invalid id"})
        except:
            return Response({"msg":"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)



    def create(self, request):
        try:
            serializer=CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                cache.delete(request.build_absolute_uri())
                #headers = self.get_success_headers(serializer.data)
                #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"msg":"Data Not created"})


    def update(self, request, pk=None):
        try:
            id=pk
            CatObj=Category.objects.get(pk=id)
            serializer=CategorySerializer(CatObj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                cache.delete(request.build_absolute_uri())
                return Response(serializer.data)
            return Response({'msg':'Something went wrong'})
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
    def destroy(self, request, pk=None):
        try:
            id = pk
            Catobj = Category.objects.get(pk=id)
            Catobj.delete()
            cache.delete(request.build_absolute_uri())
            return Response({'msg':'Data Deleted'})
        except:
            return Response({"msg":"Data deleted"})



