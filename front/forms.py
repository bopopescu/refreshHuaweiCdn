from django import forms
from .models import User


class LoginForm(forms.Form):
    name = forms.CharField(max_length=32, label="账号", widget=forms.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(max_length=32, label="密码", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        num = User.objects.filter(name=self.cleaned_data.get('name')).count()
        print(num)
        if num == 0:
            raise forms.ValidationError("账号不存在！")
        else:
            if self.cleaned_data.get("pwd") != User.objects.filter(name=self.cleaned_data.get('name')).first().pwd:
                raise forms.ValidationError("密码错误！")
        return self.cleaned_data


class RefreshForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    fresh_type = forms.ChoiceField(choices=((1, '文件'), (2, '目录')), widget=forms.RadioSelect(attrs={"class": "text-center"}))
