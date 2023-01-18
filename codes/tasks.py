import time

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379')


@app.task
def add(x, y):
    time.sleep(4)
    print(x + y)
    return x + y


@app.task
def http_request(url):
    time.sleep(4)
    print(url)
    return url


@app.task
def http_request_with_error(url):
    time.sleep(4)
    if url == 'https://www.5.com':
        raise Exception('Error')
    # print(url)
    return url


@app.task
def http_request_with_no_result(url):
    time.sleep(4)
    if not url == 'https://www.5.com':
        return url


@app.task
def convert_to_text(html):
    time.sleep(4)

    return f"Text from {html}"
