import requests
from bs4 import BeautifulSoup
import re

'''
def get_imdb_soundtrack(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/soundtrack"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error loading page for {imdb_id}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    lis = soup.find_all('li')
    return [li.get_text(strip=True) for li in lis]
'''


def get_imdb_soundtrack(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/soundtrack"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error loading page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    lis = soup.find_all('li')

    tracks = []
    for li in lis:
        text = li.get_text(strip=True)
        # Only include lines that look like soundtrack data

        if 'by' in text :
            tracks.append(text)

    return tracks
'''



def get_imdb_soundtrack(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/soundtrack"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error loading page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    blocks = soup.find_all('div', class_='soundTrack')

    tracks = []
    for block in blocks:
        for li in block.find_all('li'):
            text = li.get_text(strip=True)
            if 'by' in text:
                tracks.append(text)

    return tracks
'''


def parse_track_entry_clean(entry):
    # Extract title
    title_match = re.split(r"Written|performed|Performed|Courtesy|Lyrics by|Words and Music by", entry)
    title = title_match[0].strip()

    # Extract performer
    performer_match = re.search(
        r"(?:Performed by|performed by|Performed & Written by|Sung by|Written, Performed & Produced by|"
        r"Written and Recorded by|Recorded by|Performed & Composed by|Written & Performed by|Performed & Produced by)"
        r"\s*([\w\s\.\-&'()]+)",
        entry
    )

    artist = None
    remixer = None

    if performer_match:
        artist = performer_match.group(1)
        artist = re.split(
            r"from|Under license|Courtesy of|Published by|Written|Played at|Composed by|Produced by|"
            r"Approved by|\(c\)|Copyright|Recording|Conducted by|Recycled by",
            artist,
            flags=re.IGNORECASE
        )[0]
        artist = artist.replace("&", " & ").replace("  ", " ").strip()

        if "Remixed by" in artist:
            artist, remixer = artist.split("Remixed by", 1)
            artist = artist.strip()
            remixer = remixer.strip()

    return {
        "track": title,
        "artist": artist if artist else None,
        "remixer": remixer if remixer else None
    }
