
import sys
sys.stdin = open('2798.txt', 'r')

def JACK() :
    global best, now, cnt

    if cnt == 3 :
        if best < now <= M :
            best = now
            return

        else :
            return

    for i in range(N) :
        if not in_Hand[i] and now + Card[i] <= M :
            now += Card[i]
            in_Hand[i] = True
            cnt += 1

            JACK()

            now -= Card[i]
            in_Hand[i] = False
            cnt -= 1


N, M = map(int, input().split())
Card = list(map(int, input().split()))
in_Hand = [0] * N

best, now, cnt = 0, 0, 0

JACK()

print(best)