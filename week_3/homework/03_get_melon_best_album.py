genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같다면 고유 번호가 낮은 노래 먼저 수록한다.
# 장르 별로(Key) 우선 재생된 횟수(Value)를 저장해야 한다.
# -> Dictionary

def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        sorted_genres = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
        result = []
    for genre, _value in sorted_genres:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_index_play_array)):
            if i > 1: break
            result.append(sorted_index_play_array[i][0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!