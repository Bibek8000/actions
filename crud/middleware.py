import time
def request_timing_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = time.time() - start_time
        print(f"{request.path} took {duration} to complete with status request {response.status_code}")
        return response
    return middleware
