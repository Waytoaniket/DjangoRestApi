
from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from API.models import Advisor, Users, CallBooked
from API.serializers import AdvisorSerializer, UserSerializer, CallBookedSerializer, UserLoginSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def AddAdvisor(request):
    if request.method == 'POST':
        data = {
            'Name': request.GET.get("Name"),
            'Photourl': request.GET.get("Photourl")
        }
        serializer = AdvisorSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("")

@api_view(['POST'])
def UserRegister(request):
    if request.method == 'POST':
        data = {
            'Name': request.GET.get("Name"),
            'Email': request.GET.get("Email"),
            'Password': request.GET.get("Password"),
        }
        serializer = UserSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("")

@api_view(['POST'])
def UserLogin(request):
    if request.method == 'POST':
        data = {
            'Email': request.GET.get("Email"),
            'Password': request.GET.get("Password"),
        }
        serializer = UserLoginSerializer(data= data)
        if serializer.is_valid():
            try:
                data = Users.objects.get(Email= data['Email'] , Password= data['Password'])
            except :
                return JsonResponse(serializer.data, status=status.HTTP_401_UNAUTHORIZED) 
            IsLogin = True
            return JsonResponse(serializer.data, status=status.HTTP_200_OK) 
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("")

@api_view(['GET'])
def AdvisorList(request,id):
    if request.method == 'GET':
        Advsorlist = Advisor.objects.all()
        Advsorlist_serializer = AdvisorSerializer(Advsorlist, many=True)
        return JsonResponse(Advsorlist_serializer.data, safe=False)

@api_view(['POST'])
def BookAdvisor(request,userid,advisorid):
    if request.method == 'POST':  
        try:
            AdvisorId = Advisor.objects.get(Id=advisorid)
            UserId = Users.objects.get(Id= userid)
        except :
            print("hello")
            return JsonResponse("No Such id", status=status.HTTP_401_UNAUTHORIZED, safe=False) 
        data = {
            'Advisor': AdvisorId.Id,
            'User': UserId.Id,
            'Time': request.GET.get("Time")
        }
        print(data)
        serializer = CallBookedSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("")

@api_view(['GET'])
def BookedAdvisorList(request,userid):
    if request.method == 'GET':
        Advsorlist = CallBooked.objects.filter(User=userid)
        data = []
        for i in Advsorlist:
            data.append({"User": i.User, "Advisor": i.Advisor, "Time": i.Time})
       
        return JsonResponse(str(data), safe=False)