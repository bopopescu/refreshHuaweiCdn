from django.contrib import admin

from .models import User, Cloud, Domain, FreshLog, UserLoginLog, FreshStatus


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "addtime"]
    list_filter = ["name", "addtime"]


class CloudAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "domain_rule"]
    list_filter = ["name", "id"]


class DomainAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cate"]
    list_filter = ["cate", "name", ]


class RefreshLogAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cate", "url", "freshtime", "state"]
    list_filter = ["cate", "freshtime", "state"]


class UserLoginLogAdmin(admin.ModelAdmin):
    list_display = ["name", "logintime"]
    list_filter = ["name", "logintime"]


class FreshStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["name"]


admin.site.register(User, UserAdmin)
admin.site.register(Cloud, CloudAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(FreshLog, RefreshLogAdmin)
admin.site.register(UserLoginLog, UserLoginLogAdmin)
admin.site.register(FreshStatus, FreshStatusAdmin)