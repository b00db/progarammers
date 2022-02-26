# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # reserve와 lost의 중복 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    # reserve에서 작은 값 i부터 출발
    # 이때 i값은 최대한 앞쪽 번호에게 먼저 빌려주고 없을 경우 뒷쪽 번호에게 빌려준다
    # 빌린 학생은 lost에서 지워 못 빌린 학생만 lost에 남긴다
    # reserve에서 다음 i값을 찾아 똑같이 진행
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    # 전체 학생에서 마지막까지 못 빌린 학생의 수를 뺀다
    return n-len(set_lost)