import numpy as np

def get_average_mood(genre_mood_map, genres_a, genres_r):
    # Ensure both are lists (or convert if not)
    genres_a = genres_a if isinstance(genres_a, list) else []
    genres_r = genres_r if isinstance(genres_r, list) else []

    # Combine both lists
    combined = genres_a + genres_r

    # Filter to only genres present in the mood map
    matched = [genre_mood_map[g] for g in combined if g in genre_mood_map]

    if not matched:
        return {"valence": None, "energy": None, "danceability": None, "tempo": None}

    # Compute average
    avg = {
        "valence": sum(d["valence"] for d in matched) / len(matched),
        "energy": sum(d["energy"] for d in matched) / len(matched),
        "danceability": sum(d["danceability"] for d in matched) / len(matched),
        "tempo": sum(d["tempo"] for d in matched) / len(matched)
    }
    return avg

def normalize_features_by_movie(df, features):
    df_norm = df.copy()
    for feature in features:
        df_norm[feature + '_norm'] = df.groupby('movie')[feature].transform(
            lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() > x.min() else 0
        )
    return df_norm

def resample_mood_arc(df, movie, feature, steps=10):
    sub = df[df['movie'] == movie]
    interp = np.interp(
        np.linspace(0, 1, steps),
        sub['track_order_norm'],
        sub[feature]
    )
    return interp