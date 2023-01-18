نقشه راه:
(در حال طراحی)
1. باینری چیست و چطور همه چیز در کامپیوتر باینری است
2. اختصاص فضا در رم چطور کار می کند
3. تفاوت اختصاص رم در پایتون با برنامه های استاتیک تایپ 
4. انواع پردازش موازی
5. انواع پردازش موازی در پایتون
6. مسیج بروکر
6. سلری




اجرا به صورت تکی تکی و غیر هم زمان
```
python -m celery -A tasks worker --pool=solo --loglevel=INFO 
```

اجرا به صورت هم زمان در ویندوز

```
python -m celery -A tasks worker --pool=eventlet --loglevel=INFO
```

محدود سازی یک تسک به مقدار در دقیقه
```
python -m celery -A tasks control rate_limit tasks.add 10/m
```


```python
add.apply_async((2, 2))
add.apply_async((2, 2), queue='lopri', countdown=10)
add(2,2)
```


```python
T.delay(arg, kwarg=value)
Star arguments shortcut to .apply_async. (.delay(*args, **kwargs) calls .apply_async(args, kwargs)).

T.apply_async((arg,), {'kwarg': value})

T.apply_async(countdown=10)
executes in 10 seconds from now.

T.apply_async(eta=now + timedelta(seconds=10))
executes in 10 seconds from now, specified using eta

T.apply_async(countdown=60, expires=120)
executes in one minute from now, but expires after 2 minutes.

T.apply_async(expires=now + timedelta(days=2))
expires in 2 days, set using datetime.
```

برای استفاده از دستور های زیر باید بک اند تعریف شده باشه
```python
res.get(timeout=1)
res.get(propagate=False)
res.failed()
res.successful()
res.state  # PENDING -> STARTED -> SUCCESS or FAILURE
# @task(track_started=True) is necessary to track the state of start.

# PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
```

signiture
```python
#full
s1 = add.s(2, 2)
res = s1.delay()
res.get()
# partially
s2 = add.s(2) 
res = s2.delay(8) # resolves the partial: add(8, 2)
```
