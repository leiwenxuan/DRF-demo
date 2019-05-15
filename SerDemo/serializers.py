from rest_framework import serializers
from .models import Book


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

def my_validate(value):
    if "敏感词汇" in value.lower():
        raise serializers.ValidationError("输入的信息含有敏感词汇")
    return value

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate, ])
#     pub_time = serializers.DateField()
#     # CHOICES = ((1, "python"), (2, "linux"), (3, "go"))
#     # category = serializers.ChoiceField(choices=CHOICES)
#     category = serializers.CharField(source="get_category_display", read_only=True)
#     post_category = serializers.IntegerField(write_only=True)
#
#     publisher = PublisherSerializer(read_only=True)
#     authors = AuthorSerializer(many=True, read_only=True)
#
#     publisher_id = serializers.IntegerField(write_only=True)
#     author_list = serializers.ListField(write_only=True)
#
#     def validate_title(self, value):
#         # title必须含有python
#         if "python" in value.lower():
#             return value
#         raise serializers.ValidationError("输入的图书的名字不合法")
#
#     def validate(self, attrs):
#         # attrs 是前端传过来的所有的数据组成的字典
#         if "python" in attrs["title"] and attrs["post_category"] == 1:
#             return attrs
#         raise serializers.ValidationError("输入的图书名字或者分类不合法")
#
#     def create(self, validated_data):
#         #通过ORM操作给Book表增加数据
#         print(validated_data)
#         book_obj = Book.objects.create(title=validated_data["title"], pub_time=validated_data["pub_time"],
#                             category=validated_data["post_category"], publisher_id=validated_data["publisher_id"])
#         book_obj.authors.add(*validated_data["author_list"])
#         return book_obj
#
#     def update(self, instance, validated_data):
#         # 通过ORM更新数据
#         # instance book_obj
#         instance.title = validated_data.get("title", instance.title)
#         instance.pub_time = validated_data.get("pub_time", instance.pub_time)
#         instance.category = validated_data.get("post_category", instance.category)
#         instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
#         if validated_data.get("author_list", False):
#             instance.authors.set(validated_data["author_list"])
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    category_text = serializers.SerializerMethodField(read_only=True)
    publisher_info = serializers.SerializerMethodField(read_only=True)
    author_info = serializers.SerializerMethodField(read_only=True)
    # 方法字段
    # SerializerMethodField 会去找钩子方法 钩子方法的返回值给这个字段
    # get_字段名称
    # obj

    def get_category_text(self, obj):
        # obj就是序列化的每个模型对象 book_obj
        return obj.get_category_display()

    def get_publisher_info(self, obj):
        return {"id": obj.publisher_id, "title": obj.publisher.title}

    def get_author_info(self, obj):
        return [{"id": author.id, "name": author.name} for author in obj.authors.all()]

    class Meta:
        model = Book
        fields = "__all__"
        # fields = ["id", "title", "pub_time"]
        # exclude = ["authors"]
        # depth = 1
        # depth 让你所有的外键关系变成read_only=True
        # extra_kwargs 给默认字段加额外的参数
        extra_kwargs = {"category": {"write_only": True},
                        "publisher": {"write_only": True},
                        "authors": {"write_only": True}}
















