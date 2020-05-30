from django.shortcuts import redirect
from django.shortcuts import reverse
from django.utils.deprecation import MiddlewareMixin


class IsLogin(MiddlewareMixin):     # 中间件检查，未登录且没有写入 list 的 url 头将会被重定向到 login 界面
    list = [
        '/admin', '/account/login', '/account/register', '/account/get',
        '/test',        # for developer to test new function remember to remove it when start server
    ]

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if not request.session.get('is_login', None):
            for s in self.list:
                if request.path.startswith(s):
                    return callback(request, *callback_args, **callback_kwargs)
            return redirect(reverse('in'))
        return callback(request, *callback_args, **callback_kwargs)
