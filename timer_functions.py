import time

def setInterval(begin, end):
    while begin < end:
        print(begin)
        begin += 1
        time.sleep(1)
    print(end)

def timer(time):
    begin = 1
    while begin < time:
        print(begin)
        begin += 1
        time.sleep(1)
    print(time)

