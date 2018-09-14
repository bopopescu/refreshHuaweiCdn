from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RefreshForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserLoginLog, User, Domain, Cloud, FreshLog, FreshStatus
from front.controller.myfun import get_clound_type
from django.core.paginator import Paginator
from django.http import HttpResponse


@login_required
def index(request):
    # return redirect(reverse("front:login"))
    return render(request, 'front/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    print(form.is_valid())
    if form.is_valid():
        print(form.cleaned_data)
        user = User.objects.filter(name=form.cleaned_data.get('name')).first()
        loginlog = UserLoginLog(name=user)
        loginlog.save()
        request.session["user_name"] = form.cleaned_data.get('name')
        return redirect(reverse("front:work"))
    return render(request, 'front/login.html', {"form": form})


# @login_required
def work(request):
    if request.method == 'POST':
        form = RefreshForm(request.POST)
    else:
        form = RefreshForm()
    print(form.is_valid())
    if form.is_valid():
        content = form.cleaned_data.get("content")
        url_list = content.strip().split()
        domain_list = list(set([v.split('/')[2] for v in url_list]))
        print(domain_list)
        for url in url_list:
            status_key = None
            task_id = 0
            v = url.split('/')[2]
            cloud_type = get_clound_type(v)
            print(cloud_type)
            if cloud_type == "未知云":
                status_key = "内容错误"
                messages.add_message(request, messages.ERROR, "内容错误，未识别的域名,请注意检查url，{}".format(url))
            cloud = Cloud.objects.filter(name=cloud_type).first()
            domain = Domain.objects.filter(name=v).first()
            if not domain:
                new_domain = Domain(name=v, cate=cloud)
                new_domain.save()
            else:
                domain.cate = cloud
                domain.save()
            domain = Domain.objects.filter(name=v).first()
            # 域名+平台判断完毕，平台名称不是“未知云”则开始调用刷新接口
            if cloud_type != "未知云":
                try:
                    # 开始执行刷新接口
                    status_key = "已提交"
                    messages.add_message(request, messages.SUCCESS, "{},提交成功，稍后可在操作记录中查看状态！".format(url))
                    # 获得task_id
                    task_id = 1
                except Exception as e:
                    status_key = "提交失败"
                    messages.add_message(request, messages.ERROR, "提交失败，{}，请尝试重新提交！".format(url))

            user_name = request.session.get("user_name")
            user = User.objects.filter(name=user_name).first()
            if status_key is not None:
                status = FreshStatus.objects.filter(name=status_key).first()
            else:
                status = FreshStatus.objects.filter(name="已提交").first()
            fresh_log = FreshLog(name=domain, cate=cloud, url=url, user=user, state=status, task_id=task_id)
            fresh_log.save()
    return render(request, 'front/work.html', {"form": form})


def refresh_log(request, page=1):
    user_name = request.session.get("user_name")
    user = User.objects.filter(name=user_name).first()
    log = FreshLog.objects.filter(user=user).order_by('-freshtime').all()
    paginator = Paginator(log, 10)
    if page > paginator.num_pages:
        page = paginator.num_pages
    elif page <= 0:
        page = 1
    elif page is None:
        page = 1
    loaded = paginator.page(page)
    print(paginator.num_pages)
    return render(request, "front/refreshlog.html", {"log": loaded})


def connect_admin(request):
    return render(request, "front/connect_admin.html")



def logout(request):
    del request.session["user_name"]
    return redirect(reverse("front:login"))

