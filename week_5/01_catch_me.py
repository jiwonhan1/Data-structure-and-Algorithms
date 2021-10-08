from collections import deque

# 2019년 상반기 LINE 인턴 채용 코딩테스트

# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다

c = 11  # 코니의 처음 위치
b = 2   # 브라운의 처음 위치

# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직임
# 속도
# 1 2 3 4 5 6 7 8 9
# 위치
# 12 14 17 21 26 32 39 47 56

# 브라운의 위치 변화
# B - 1, B + 1, 2 * B
# 2
# 1-1. 1
# 1-2. 3
# 1-3. 4

# 1-1-1. 0
# 1-1-2. 2
# 1-1-3. 2

# 모든 경우의 수 나열
# => BFS

# 잡았다!라는 의미는
# 똑같은 시간에 똑같은 위치에 존재해야 함
# 시간은 + 1
# 위치는 코니도 브라운도 값이 자유자재로 바뀐다
# 규칙적 => 배열, 자유자재 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장
# -> [{}]
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # 위치와 시간을 동시에 담는다
    visited = [{} for _ in range(200001)] # visited[위치][시간]
    # visited[0] = {
    #   2: True
    # }
    # => 위치 0에 2초
    # visited[1] = {
    # 1: True
    # 3: True
    # 4: True
    # }
    # => 1 방문에 1,3,4 시간
    # visited[cony_loc][time] 키 값 존재? => true
    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position <= 2000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position <= 2000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        print(visited)
        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!