from django.shortcuts import redirect


def redirect_login_users(func: callable):
    """
    A decorator function that checks whether the user trying to access the page
    is authorized or not, if authorized, then redirect him to the main page of the
    site otherwise - show the content of this page
    :param func: view-function, which is responsible for processing the page,
    the content of which we want
    to close from users who are already authorized on the site
    (registration or authorization page)
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_page')
        func(request, *args, **kwargs)
    return wrapper


