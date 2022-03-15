#https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # scoville을 힙으로 변환
    
    while scoville[0] < K:  # scoville의 가장 작은 값이 K를 넘지 않는 동안 반복
        mix_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix_scoville)
        answer += 1
        
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer