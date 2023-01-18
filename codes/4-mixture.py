from celery import chord
from tasks import http_request, convert_to_text

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

result = chord((http_request.s(url) for url in request_pool), convert_to_text.s())()
print(result.get())


