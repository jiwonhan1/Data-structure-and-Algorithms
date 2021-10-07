current_r, current_c, current_d = 7, 4, 0

# 전부 탐색하고 모든 칸을 탐색한다면 BFS

# 1. 현재 위치를 청소한다
# bfs 구현 visited = [1, 2, 3]
# 0 은 청소 안한 장소
# 1 은 청소 못하는 장소
# 2 는 청소한 장소


current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행한다
# -> 방향
# 북쪽으로 가면 row -1 col 0
# 동족 row 0 col 1
# 남쪽 row +1 col 0
# 서쪽 row 0 col -1
# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
# 그 방향으로 회전한 다음 전진하고 1번부터 진행한다

# b. 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하고 2번으로 돌아간다
# -> 현재 본 방향에서 청소할 곳이 없다면 다시 왼쪽으로 회전하라는 의미

# c. 네 방향 모두 청소가 되어 있거나 벽인 경우에는 바라보는 방향을 유지한채로 한칸 후진을 하고 2번으로 돌아간다
# -> 모든 방향이 청소 되어있다면 뒤로 한칸 후진
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# north to west => 0 -> 3
# west to south => 3 -> 2
# south to east => 2 -> 1
# east to north => 1 -> 0

# north to back => 0 -> 2
# east to back => 1 -> 3
# south to back => 2 -> 0
# west to back => 3 -> 1

# d. 네 방향 모두 청소가 되어 있거나 벽이면서,
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우엔 작동을 멈춘다

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

def get_d_index_when_go_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    count_of_departments_cleaned = 1 # 맨 처음칸은 청소했다고 쳐서 1로 initialized
    n = len(room_map)
    m = len(room_map[0])
    room_map[r][c] = 2
    queue = list([[r, c, d]])
    while queue:
        r, c, d = queue.pop(0)
        temp_d = d
        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned
    # return
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))