import time

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n-=1
    print(n)

def recursive_countdown(n):
    if n < 0:
        return
    print(n)
    time.sleep(1)
    return recursive_countdown(n-1)
recursive_countdown(6)