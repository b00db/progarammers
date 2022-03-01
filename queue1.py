# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    count = 0  # 베포 수
    day = 0  # 일 수
    
    while len(progresses)>0:
        # 먼저 queue에 들어온 작업부터 count를 저장 후 pop으로 내보내기
        if(progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            day += 1
            if count > 0:
                answer.append(count)
                count = 0
    # 마지막 queue에 있던 작업의 count를 append
    answer.append(count)
    return answer