'''
- 번호 : 1244
- 제목 : 스위치 켜고 끄기
'''

import sys
input = sys.stdin.readline

def flip(_input):
    return 1 if _input == 0 else 0

N = int(input())
switches = list(map(int,input().split()))

R = int(input())
for _ in range(R):
    gender, idx = map(int, input().split())
    
    # 남자의 경우
    if gender == 1:
        # 배수에 해당하는 모든 스위치 On-Off 변경
        while idx < N:
            switches[idx-1] = flip(switches[idx-1])
            idx += idx
    
    elif gender == 2:
        i = idx - 2
        j = idx
        switches[idx-1] = flip(switches[idx-1])
        while (-1 < i < N) and (-1 < j < N):
            # 좌우 스위치가 같으면
            if switches[i] == switches[j]:
                # 스위치의 상태를 변경함
                switches[i] = flip(switches[i])
                switches[j] = flip(switches[j])
                # 다음 탐색을 준비함
                i = i - 1
                j = j + 1
            # 좌우 스위치가 다르면 멈춤
            else:
                break
    
print(*switches)