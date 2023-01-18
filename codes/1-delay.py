import time

from tasks import add

# result = add.delay(2, 2)
# result2 = add.delay(3, 3)


add.delay(2, 2)
add.delay(3, 3)



# for i in range(10):
#     time.sleep(1)
#     print(result.ready())
