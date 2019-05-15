from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.throttle import MyThrottle, MyVisit

# Create your views here.


class TestView(APIView):
    throttle_classes = [MyVisit, ]

    def get(self, request):
        return Response("频率测试接口")
