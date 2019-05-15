from rest_framework import authentication
from AuthDemo.models import User
from rest_framework.exceptions import AuthenticationFailed


class MyAuth(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        # 获取前端携带的token
        # 去比对这个token是否合法
        token = request.query_params.get("token", "")
        if not token:
            raise AuthenticationFailed("没有携带token")
        user_obj = User.objects.filter(token=token).first()
        if user_obj:
            return (user_obj, token)
        raise AuthenticationFailed("token不合法")
    