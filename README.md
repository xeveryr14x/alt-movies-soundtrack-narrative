# alt-movies-narrative-soundtrack
This project explores **emotional arcs and narrative structures** in alternative or cult coming-of-age films with punk, anarchist, or nihilist elements, using their **soundtracks** as the emotional proxy.

## Motivation
Movies tell stories through music, especially in punk, alternative, and indie films, where raw and genre-driven soundtracks shape the emotional fabric of a scene. These rebellious and emotionally rich (or introspective) films don’t just entertain; they push back, reflect angst, and speak to identity and disillusionment. **But what exactly are they telling us? What values, moods, and messages are embedded in their soundscapes?**

This project explores how we can model those emotions quantitatively, using soundtrack metadata, inferred audio features (valence, energy, danceability, tempo), and time series analysis to map the emotional arcs of cult and countercultural cinema. Much of the inspiration came from exploring films on [Tubi](https://tubitv.com/), whose unique catalog of punk, indie, and outsider stories helped shape the emotional lens of this work. 

## Emotional Landscape
The map below clusters 20 cult punk and indie films into **6 emotional archetypes** purely based on their soundtracks. Each point represents a film; clusters capture shared arcs and values, from “Detached Nihilism” to “Chaotic Surrealism”.

![t-SNE Projection](plots/tsne_projection_clusters.png)

*Each cluster reveals a distinct narrative mood shaped by emotional dynamics in the soundtrack.*


## Features
- 20 niche movie list curation (coming-of-age, punk, anarchist, nihilist, suburbs, indie, low-budget)
- IMDb soundtrack scraping and cleaning
- Track title + artist extraction, including edge cases (e.g., remixers, missing performers)
- Genre tagging (based on artist metadata through Spotify APIs)
- Audio feature inference by genre using curated JSON mappings (183 music genres)
- Normalization + time series interpolation of emotional features per film
- PCA & KMeans clustering optimization
- Visualization using t-SNE 
- Cluster-based analysis of emotional archetypes
- Exported datasets and genre mappings

## Cluster Description
| Cluster Name                | Description |
|----------------------------|-------------|
| Detached Nihilism          | Emotionally flat, observational, ironic |
| Rebel Without Resolution   | Punk identity vs. real-world collapse |
| Outsider Bloom             | Queer/feminine identity through tender rebellion |
| Lonely Drifter             | Poetic solitude and inward journeys |
| Haunting Realism           | Slow-burn narratives with moral weight |
| Chaotic Surrealism         | Fragmented, dreamlike, emotionally volatile |


## Results
This project demonstrates that we can **decode a film’s emotional and narrative flow by analyzing the order and genre of its soundtracks**, even without watching the movie.

**Soundtracks as Emotional Arcs**
By mapping each track to valence, energy, danceability, and tempo (inferred from genres), and preserving the track order from the film, we created a quantitative emotional arc for each movie. These arcs visualize how a film moves through moods like tension, euphoria, melancholy, or chaos, often mirroring plot developments or character evolution.

*In alternative and indie cinema, where storylines can be loose or nonlinear, the soundtrack often carries the emotional structure. This project treats that as a signal.*

**Emotional Landscape via t-SNE**
To visualize high-dimensional emotional arcs, I projected films into 2D space using t-SNE. This made it possible to see thematic proximity like how two movies with wildly different plots might share one similiar emotional rhythm.

## Credits
Project by Yiran Ren (xeveryr14x@github)

Built using data from IMDb, Spotify, and genre-based acoustic mappings.

## License
This project is for academic/educational use only. Not affiliated with IMDb or Spotify.
