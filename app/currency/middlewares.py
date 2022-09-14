from time import time
from currency.models import ResponseLog


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        request_method = request.method
        query_params = request.GET
        ip = request.META['REMOTE_ADDR']
        path = request.path
        response = self.get_response(request)
        end = time()
        response_time = end - start
        ResponseLog.objects.create(
            response_time=response_time,
            request_method=request_method,
            query_params=query_params,
            ip=ip,
            path=path
        )

        return response
