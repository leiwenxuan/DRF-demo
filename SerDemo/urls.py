from django.conf.urls import url, include
from .views import BookView, BooksView, BookEditView, BookModelView
from rest_framework.routers import DefaultRouter

# 第一步实例化对象
router = DefaultRouter()
# 第二步把路由以及视图注册
router.register('list', BookModelView)

urlpatterns = [
    # url(r'^list$', BookView.as_view()),
    # url(r'^list$', BooksView.as_view()),
    # url(r'^list$', BookModelView.as_view({"get": "list", "post": "create"})),
    # url(r'^retrieve/(?P<id>\d+)$', BookEditView.as_view()),
    # url(r'^retrieve/(?P<pk>\d+)$', BookModelView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]
# 第三步 把生成好的路由注册进去
urlpatterns += router.urls

# as_view 分发
# dispatch
# get---self.get

# 重写as_view  get---传参的字典里对应的方法
