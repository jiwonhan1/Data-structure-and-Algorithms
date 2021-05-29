from collections import deque

c = 11
b = 2

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

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]
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