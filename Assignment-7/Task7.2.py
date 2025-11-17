def count_down(n):
    while n >= 0:
        print(n)
        n -= 1  # Fixed: changed from n += 1 to n -= 1 to properly count down
