'''
- 번호 : 1713
- 제목 : 후보 추천하기
'''

import sys
input = sys.stdin.readline


N = int(input())
R = int(input())
A = list(map(int, input().split()))

nominee = [0] * N
score = [0] * N

for i in range(R):
    if A[i] in nominee: # 사진이 이미 걸려있다면
        score[nominee.index(A[i])] += 1
    else : # 사진이 걸려있지 않은 상태에서
        # 프레임에 빈 공간이 있다면,
        if 0 in nominee:
            idx = nominee.index(0)
            nominee[idx] = A[i]
            score[idx] = 1
        # 프레임에 빈 공간이 없다면,
        else:
            # 최소 추천 사진을 찾는다
            idx = score.index(min(score))
            # 최소 추천 사진을 빼고 뒤에 있는 사진들을 앞으로 당긴다.
            nominee = nominee[:idx] + nominee[idx+1:] + [A[i]]
            score = score[:idx] + score[idx+1:] + [A[i]]

nominee.sort()
print(*nominee)