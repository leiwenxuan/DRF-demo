from rest_framework import versioning

class MyVersion(object):

    def determine_version(self, request, *args, **kwargs):
        # 拿版本号
        version = request.query_params.get("version", "v1")
        return version

