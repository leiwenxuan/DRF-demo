from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):

    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            # 证明它是复杂请求先发预检
            response["Access-Control-Allow-Methods"] = "DELETE"
            response["Access-Control-Allow-Headers"] = "Content-Type"
        return response