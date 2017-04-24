import django.http


def ajax_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            raise django.http.HttpResponse(status=403)
        return func(request, *args, **kwargs)

    return wrapper
