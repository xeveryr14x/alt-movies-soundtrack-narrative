# punk-narrative-soundtrack
This project explores **emotional arcs and narrative structures** in cult and coming-of-age films with punk, anarchist, or nihilist elements — using their **soundtracks** as the emotional proxy.

## Motivation
Movies tell stories through music. Especially when punk, alternative, and indie films often use raw, genre-driven soundtracks to shape emotional texture. At the end of the day, what do these rebellious movies convey to us? How do their narratives shape the values that impact the audience?

This project explores how we can model that emotion quantitatively—using track metadata, inferred audio features (valence, energy, danceability, tempo), and time series analysis.

## Features
- 20 niche movie list curation (punk, anarchist, nihilist, urban decay, coming-of-age, indie, low-budget)
- IMDb soundtrack scraping and cleaning
- Track title + artist extraction, including edge cases (e.g., remixers, missing performers)
- Genre tagging (based on artist metadata through Spotify APIs)
- Audio feature inference by genre using curated JSON mappings
- Normalization + time series interpolation of emotional features per film
- Mood arc visualizations & PCA clustering of films
- Cluster-based analysis of emotional archetypes
- Exported datasets and genre mappings

## Sample Movies
- SLC Punk! (1998)
- Suburbia (1983 & 1996)
- Smithereens (1982)
- Ghost World (2001)
- Nowhere (1997)
- Ladies and Gentlemen, the Fabulous Stains (1982)
- Slacker (1990)

