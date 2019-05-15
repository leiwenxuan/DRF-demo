from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    token = models.UUIDField(null=True, blank=True)
    CHOICES = ((1, "vip"), (2, "普通用户"), (3, "vvip"))
    type = models.IntegerField(choices=CHOICES, default=2)
