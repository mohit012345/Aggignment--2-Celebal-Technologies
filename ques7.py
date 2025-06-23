t = int(input())

for _ in range(t):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)