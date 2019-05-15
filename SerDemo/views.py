from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Book, Publisher
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import BookSerializer
from rest_framework.viewsets import ViewSetMixin
import json
# Create your views here.

# book_list = [
#     {
#         "id": 1,
#         "title": "",
#         "publisher": {
#              "id": 1
#               "title": ""
#           },
#          "authors": [{}]
#     },
#     {
#
#     }
# ]


class BookView(View):
    # 第一版用.values实现序列化
    # def get(self, request):
    #     book_queryset = Book.objects.values("id", "title", "pub_time", "publisher")
    #     # queryset [{}, {}]
    #     book_list = list(book_queryset)
    #     ret = json.dumps(book_list, ensure_ascii=False)
        # return HttpResponse(ret)
    #     ret = []
    #     for book in book_list:
    #         publisher_obj = Publisher.objects.filter(id=book["publisher"]).first()
    #         book["publisher"] = {
    #             "id": publisher_obj.id,
    #             "title": publisher_obj.title
    #         }
    #         ret.append(book)
    #     return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})

    # 第二版
    def get(self, request):
        book_queryset = Book.objects.all()
        ret = serializers.serialize("json", book_queryset, ensure_ascii=False)
        return HttpResponse(ret)
######################################################
# 把5个方法抽离出来

###################初始版本###################
#
# class BooksView(APIView):
#
#     def get(self, request):
#         queryset = Book.objects.all()
#         ser_obj = BookSerializer(queryset, many=True)
#         return Response(ser_obj.data)
#
#
#     def post(self, request):
#         ser_obj = BookSerializer(data=request.data)
#         if ser_obj.is_valid():
#             ser_obj.save()
#             return Response(ser_obj.data)
#         return Response(ser_obj.errors)





######################第一次封装#################

class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):
    def list(self, request):
        queryset = self.get_queryset()
        ser_obj = self.get_serializer(queryset, many=True)
        return Response(ser_obj.data)


class CreateModelMixin(object):
    def create(self, request):
        ser_obj = self.get_serializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        obj = self.get_queryset().filter(id=id).first()
        ser_obj = self.get_serializer(obj)
        return Response(ser_obj.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ser_obj = self.get_serializer(instance=book_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors)


class DestroyModelMixin(object):
    def destroy(self, request, id):
        obj = self.get_queryset().filter(id=id).first()
        if obj:
            obj.delete()
            return Response("")
        return Response("删除的对象不存在")


class BooksView(GenericAPIView, ListModelMixin, CreateModelMixin):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        # queryset = self.get_queryset()
        # ser_obj = self.get_serializer(queryset, many=True)
        # return Response(ser_obj.data)
        return self.list(request)

    def post(self, request):
        # ser_obj = BookSerializer(data=request.data)
        # if ser_obj.is_valid():
        #     ser_obj.save()
        #     return Response(ser_obj.data)
        # return Response(ser_obj.errors)
        return self.create(request)


class BookEditView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # ser_obj = BookSerializer(book_obj)
        # return Response(ser_obj.data)
        return self.retrieve(request, id)

    def put(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # ser_obj = BookSerializer(instance=book_obj, data=request.data, partial=True)
        # if ser_obj.is_valid():
        #     ser_obj.save()
        #     return Response(ser_obj.data)
        # return Response(ser_obj.errors)
        return self.update(request, id)

    def delete(self, request, id):
        # book_obj = Book.objects.filter(id=id).first()
        # if book_obj:
        #     book_obj.delete()
        #     return Response("")
        # return Response("删除的对象不存在")
        return self.destroy(request, id)


############第二次封装#############
# 方便继承

###########第三次封装############
from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView

class ModelViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin, DestroyModelMixin):
    pass


# class BookModelView(ModelViewSet):
#     query_set = Book.objects.all()
#     serializer_class = BookSerializer

#########所有的视图类###########
from rest_framework import views
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

######## 用框架提供的ModelViewSet
from rest_framework.viewsets import ModelViewSet


class BookModelView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

# 框架默认会把queryset结果进行缓存





























