# 以IP地址做限流
# 1 获取访问者的IP地址
# 2 访问列表 {IP: [time2, time1]}
# 3 判断IP是否在我们的访问列表里
# 4 如果不在 第一次访问 给访问列表加入IP：[now]
# 5 如果在 把now放入IP：[now, time2, time1]
# 6 确保列表里最近的访问时间以及最远的访问时间差在限制时间范围内
# 7 判断列表长度是否是限制次数之内
from rest_framework import throttling
import time
# [now, 5, 4, 3, 2, old]


# 60秒访问3次
class MyThrottle(throttling.BaseThrottle):
    VisitRecord = {}
    def __init__(self):
        self.history = ""

    def allow_request(self, request, view):
        # 做频率限流
        ip = request.META.get("REMOTE_ADDR")
        now = time.time()
        if ip not in self.VisitRecord:
            self.VisitRecord[ip] = [now,]
            return True
        history = self.VisitRecord.get(ip)
        # self.history = self.cache.get(self.key, [])
        history.insert(0, now)
        self.history = history
        while history and history[0] - history[-1] > 60:
            history.pop()
        if len(history) > 3:
            return False
        else:
            return True

    def wait(self):
        # 还要等多久才能访问
        # old + 60 - now
        return self.history[-1] + 60 - self.history[0]


class MyVisit(throttling.SimpleRateThrottle):
    scope = "WD"

    def get_cache_key(self, request, view):
        # 返回值应该IP
        return self.get_ident(request)
