# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # 각 수포자가 찍는 방식
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 각 수포자들이 맞힌 문제의 개수
    count1 = 0
    count2 = 0
    count3 = 0
    
    # 완전탐색 _ 모든 경우의 수를 다 계산
    for i in range(len(answers)):
        if answers[i] == answer1[i%5]:
            count1 += 1
        if answers[i] == answer2[i%8]:
            count2 += 1
        if answers[i] == answer3[i%10]:
            count3 += 1
    
    # 가장 높은 점수를 받은 사람을 저장, 여럿일 경우 오름차순 정렬
    max_count = max(count1, count2, count3)
    answer = []
    if max_count == count1:
        answer.append(1)
    if max_count == count2:
        answer.append(2)
    if max_count == count3:
        answer.append(3)
    
    return answer