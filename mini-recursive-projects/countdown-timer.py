import time

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n-=1
    print(n)

    