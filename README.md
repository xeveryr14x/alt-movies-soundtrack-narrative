# punk-narrative-soundtrack
This project explores **emotional arcs and narrative structures** in cult and coming-of-age films with punk, anarchist, or nihilist elements — using their **soundtracks** as the emotional proxy.

**Motivation**
Movies tell stories through music. Especially punk, alternative, and indie films often use raw, genre-driven soundtracks to shape emotional texture. This project explores how we can model that emotion quantitatively—using track metadata, inferred audio features (valence, energy, danceability, tempo), and time series analysis.


## 📦 Features
- 🧹 IMDb soundtrack scraping and cleaning
- 🎵 Track title + artist extraction, including edge cases (e.g., remixers, missing performers)
- 🏷️ Genre tagging (based on artist metadata or manual assignment)
- 🔊 Audio feature inference by genre using curated JSON mappings
- 📈 Normalization + time series interpolation of emotional features per film
- 🎨 Mood arc visualizations & PCA clustering of films
- 🔍 Cluster-based analysis of emotional archetypes
- 📁 Exported datasets and genre mappings
I scrape soundtrack data from IMDb, extract track-level features using genre mappings, and analyze emotional progressions using time series and clustering techniques.
