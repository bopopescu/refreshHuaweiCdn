from django.db import models


class User(models.Model):
    name = models.CharField(unique=True, max_length=32, null=False)
    pwd = models.CharField(max_length=320, null=False)
    addtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(unique=True, max_length=32, null=False)
    cate = models.ForeignKey("Cloud", on_delete=False)

    def __str__(self):
        return self.name


class Cloud(models.Model):
    name = models.CharField(unique=True, max_length=32, null=False)
    domain_rule = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class FreshStatus(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class FreshLog(models.Model):
    user = models.ForeignKey("User", on_delete=False)
    name = models.ForeignKey("Domain", on_delete=False)
    cate = models.ForeignKey("Cloud", on_delete=False)
    url = models.CharField(max_length=120)
    freshtime = models.DateTimeField(auto_now=True)
    state = models.ForeignKey("FreshStatus", on_delete=False)
    task_id = models.CharField(max_length=32)
    # def __str__(self):
    #     return self.id


class UserLoginLog(models.Model):
    name = models.ForeignKey("User", on_delete=False)
    logintime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name