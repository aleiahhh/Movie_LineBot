import requests

now_playing_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=25404cdd3ef139c8f4f75f50d83c8a72&language=en-US&page=1'
popular_url = 'https://api.themoviedb.org/3/movie/popular?api_key=25404cdd3ef139c8f4f75f50d83c8a72&language=en-US&page=1'
top_rated_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=25404cdd3ef139c8f4f75f50d83c8a72&language=en-US&page=1'
upcoming_url = 'https://api.themoviedb.org/3/movie/upcoming?api_key=25404cdd3ef139c8f4f75f50d83c8a72&language=en-US&page=1'

def get_now_playing():
    now_playing_json = requests.get(now_playing_url).json()
    now_playing = now_playing_json['results']
    data = []
    for row in now_playing:
        row_data = []
        row_data.append(row['title'])
        row_data.append(row['popularity'])
        row_data.append(row['vote_average'])
        row_data.append(row['original_language'])
        row_data.append(row['adult'])
        row_data.append(row['overview'])
        row_data.append(row['poster_path'])
        data.append(row_data)
    return data

def get_popular():
    popular_json = requests.get(popular_url).json()
    popular = popular_json['results']
    data = []
    for row in popular:
        row_data = []
        row_data.append(row['title'])
        row_data.append(row['popularity'])
        row_data.append(row['vote_average'])
        row_data.append(row['original_language'])
        row_data.append(row['adult'])
        row_data.append(row['overview'])
        row_data.append(row['poster_path'])
        data.append(row_data)
    return data

def get_top_rated():
    top_rated_json = requests.get(top_rated_url).json()
    top_rated = top_rated_json['results']
    data = []
    for row in top_rated:
        row_data = []
        row_data.append(row['title'])
        row_data.append(row['popularity'])
        row_data.append(row['vote_average'])
        row_data.append(row['original_language'])
        row_data.append(row['adult'])
        row_data.append(row['overview'])
        row_data.append(row['poster_path'])
        data.append(row_data)
    return data

def get_upcoming():
    upcoming_json = requests.get(upcoming_url).json()
    upcoming = upcoming_json['results']
    data = []
    for row in upcoming:
        row_data = []
        row_data.append(row['title'])
        row_data.append(row['popularity'])
        row_data.append(row['vote_average'])
        row_data.append(row['original_language'])
        row_data.append(row['adult'])
        row_data.append(row['overview'])
        row_data.append(row['poster_path'])
        data.append(row_data)
    return data

print(get_now_playing())