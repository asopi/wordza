from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """
    This decorator checks if the user is unauthenticated and returns the view function.
    If the user is already authenticated, he will be redirected to a blank URL.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
