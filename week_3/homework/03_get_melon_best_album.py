genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


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