H = int(input())

def f(h):
    if h == 1:
        return 1
    else:
        return 1+2*f(h//2)

print(f(H))