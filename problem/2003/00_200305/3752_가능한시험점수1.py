for test in range(1, int(input()) + 1):
    input()
    points = map(int, input().split())
    ans = 1
    for point in points:
        ans |= ans << point
    print('#%d' % test, bin(ans).count('1'))