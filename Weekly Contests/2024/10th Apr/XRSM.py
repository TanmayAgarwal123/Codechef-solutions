# cook your dish here
import math
import sys
from collections import defaultdict
import itertools
from itertools import permutations, combinations
from collections import Counter
from collections import deque
from math import gcd, lcm, ceil, floor, factorial, isqrt, prod, sqrt, log2, log10, inf
import heapq
from heapq import heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right

# sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n%2 == 0:
        return n == 2
    if n%3 == 0:
        return n == 3
    
    for i in range(5, isqrt(n) + 1, 6):
        if n%i == 0 or n%(i + 2) == 0:
            return False
    return True

gi = lambda: list(map(int, input().split()))
gs = lambda: list(map(str, input().split()))

binary = lambda x: bin(x)[2:]
decimal = lambda x: int(x, 2)


# primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def tests() -> int:
    n, s = gi()
    if s < n or s%2==1 or n==1:
        print(-1)
        return 0
    
    bs = binary(s)
    l = [int(x) for x in bs]
    for i in range(len(bs)):
        if l[i]%2==1:
            if i==len(bs)-1:
                print(-1)
                return 0
            l[i] -= 1
            l[i+1] += 2
    sl = sum(l)
    

    while sl < n:
        i = len(bs)-2
        while i!=-1 and l[i] == 0:
            i -= 1
        l[i] -= 2
        l[i+1] += 4
        sl += 2

    
    
    ans = []
    base = 1
    l.reverse()
    for i in range(len(l)):
        ans.extend([base]*l[i])
        base *= 2
    # print(ans)
    if len(ans) - n == 1:
        if ans[0] == ans[-1]:
            print(-1)
            return 0
        ans[0] += ans[-1]
        ans.pop()
        print(*ans)
        return 0
    if len(ans) == n:
        print(*ans)
        return 0
    # print(ans)
    k = len(ans)
    ans = ans[0:k:2] + ans[1:k:2]
    while len(ans) > n:
        # print(ans)
        k = len(ans)
        ans2 = []
        i = 0
        while i < len(ans):
            # print(i, ans2)
            if i == len(ans)//2 - 1 and len(ans)%4!=0:
                ans2.append(ans[i])
                i += 1
                continue
            if i + 1 == len(ans):
                ans2.append(ans[i])
                i += 1
                continue
            ans2.append(ans[i] + ans[i+1])
            k -= 1
            if k == n:
                ans = ans2 + ans[i+2:]
                break
            i += 2
        else:
            ans = ans2
    print(*ans)


    return 0

def main() -> int:
    t = 1
    t = int(input())
    for _ in range(t):
        tests()
    return 0

if __name__ == "__main__":
    main()