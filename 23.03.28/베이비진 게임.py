import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

def baby(cards):
    runs = tri = 0
    a = 0
    while a < 8:
        if cards[a] >= 3:
            cards[a] -= 3
            tri += 1
            continue
        if cards[a] >= 1 and cards[a+1] >= 1 and cards[a+2] >= 1:
            cards[a] -= 1
            cards[a+1] -= 1
            cards[a+2] -= 1
            runs += 1

t = int(input())
for tc in range(1, t+1):
    cards = list(map(int,input().split()))

    p1 = [0] * 10
    p2 = [0] * 10

    ans = 0

