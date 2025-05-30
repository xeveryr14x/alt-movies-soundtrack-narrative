def get_artist_genres(sp, artist_name):
    try:
        result = sp.search(q=f"artist:{artist_name}", type="artist", limit=1)
        items = result['artists']['items']
        if items:
            return items[0]['genres']
        else:
            return []
    except Exception as e:
        print(f"Error for artist '{artist_name}': {e}")
        return []
