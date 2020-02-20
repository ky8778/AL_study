N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_cnt = A[0]
    A_card = A[1:]
    B_cnt = B[0]
    B_card = B [1:]
    A_card.sort(reverse=True)
    B_card.sort(reverse=True)
    for j in range(max(A_cnt,B_cnt)):
        if A_cnt != B_cnt and (A_cnt - 1 < j or B_cnt - 1 < j):
            if A_cnt > B_cnt:
                print('A')
                break
            else:
                print('B')
                break
        elif A_card[j] > B_card[j]:
            print('A')
            break
        elif A_card[j] < B_card[j]:
            print('B')
            break
        elif A_cnt - 1 == j and B_cnt - 1 == j:
            print('D')