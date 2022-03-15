## https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # 두 리스트를 정렬
    participant.sort()
    completion.sort()
    # 두 리스트를 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 비교해도 없으면 participant의 마지막 선수가 완주하지 못한 선수
    return participant[len(participant)-1]