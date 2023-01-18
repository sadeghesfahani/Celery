from celery import group

from tasks import http_request, http_request_with_error, http_request_with_no_result

request_pool = [
    'https://www.1.com',
    'https://www.2.com',
    'https://www.3.com',
    'https://www.4.com',
    'https://www.5.com',
    'https://www.6.com',
    'https://www.7.com',
    'https://www.8.com',
]

results = group(http_request.s(url) for url in request_pool)().get()
print(results)


results = group(http_request_with_no_result.s(url) for url in request_pool)().get()
print(results)


results = group(http_request_with_error.s(url) for url in request_pool)().get()
print(results)
