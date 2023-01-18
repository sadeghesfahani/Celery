from celery import chain
from tasks import http_request, convert_to_text

result = chain(http_request.s('https://www.1.com') | convert_to_text.s())()
# print(result.get())  # see how it block the flow
print("here")