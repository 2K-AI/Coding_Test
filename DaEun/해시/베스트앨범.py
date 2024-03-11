def solution(genres, plays):
    import pandas as pd
    answer = []
    new = [ [g,p]for g,p in zip(genres, plays)]
    df = pd.DataFrame(new, columns=['genre','play'])
    genre_sort = list(df.groupby('genre')['play'].sum().sort_values(ascending = False).index)
    for g in genre_sort:
        answer = answer+list(df[df.genre==g].sort_values(by='play', ascending=False)[:2].index)
    return answer
