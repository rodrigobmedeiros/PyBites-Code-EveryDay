def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    
    if start < 1:
        print('time is up')
        return

    print(start)
    countdown_recursive(start - 1)