from django.shortcuts import redirect

def logout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # ya jo bhi home ho
        return view_func(request, *args, **kwargs)
    return wrapper
