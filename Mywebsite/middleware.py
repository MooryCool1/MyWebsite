from django.http import HttpResponsePermanentRedirect


class RedirectWWWMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host.startswith('www.'):
            new_host = host[4:]
            url = f'https://{new_host}{request.get_full_path()}'
            return HttpResponsePermanentRedirect(url)
        return self.get_response(request)