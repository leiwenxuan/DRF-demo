from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class DemoView(APIView):
    def get(self, request, version):
        print(request.version)
        print(request.versioning_scheme)
        if request.version == "v1":
            return Response("夏雨豪和文周的粉色回忆")
        elif request.version == "v2":
            return Response("夏雨豪和文周的不能说的秘密")
        return Response("版本不合法")
