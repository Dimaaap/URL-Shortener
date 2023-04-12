from django.shortcuts import redirect


def redirect_login_users(func: callable):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_page')
        return func(request, *args, **kwargs)
    return wrapper


