''' Question: 베스트앨범
*   https://programmers.co.kr/learn/courses/30/lessons/42579/
'''


def solution(genres, plays):
    def update_bests(bests, song_id):
        bests.append(song_id)
        bests.sort(reverse=True, key=lambda x: plays[x])
        if len(bests) > 2:
            bests.pop()
        if bests[0] == bests[1]:
            bests.sort()

    plays_genre = {}
    bests_genre = {}

    for i, play in enumerate(plays):
        genre = genres[i]
        if genre not in plays_genre:
            plays_genre[genre] = play
            bests_genre[genre] = [i]
        else:
            plays_genre[genre] += play
            update_bests(bests_genre[genre], i)

    keys = list(plays_genre.keys())
    keys.sort(reverse=True, key=lambda x: plays_genre[x])

    result = []
    for key in keys:
        result.extend(bests_genre[key])

    return result
