# Philly Thanksgiving trip page

The whole site is `index.html`: plain HTML, no CSS. The only JS is the inline `onclick` on the two buttons (Show all reviews / Collapse all). Keep it that way unless the user asks otherwise.

Each place is one `<tr>` in the Museums or Food table. Its reviews sit in a `<details>` in the first cell. The Map cell links to Google Maps in a new tab.

## Adding a place: always add reviews

Every time a place is added, look up and fill in both review sources before publishing:

1. Google: run `python3 -I scripts/google_rating.py "<Place Name> Philadelphia"`. Check that `gname` is the right place, then use its `rating`, `count` and `url`.
2. TripAdvisor: search `tripadvisor <Place Name> Philadelphia` and take the rating, review count and listing URL from the Philadelphia listing. Never guess numbers.
3. Copy an existing `<tr>` block and fill it in, using the same wording:
   - `Google: 4.7 ★ (310 reviews) <a href="..." target="_blank">read reviews</a>`
   - A listing with no reviews: `TripAdvisor: no reviews yet (<a href="..." target="_blank">view listing</a>)`
   - No listing: `TripAdvisor: no listing found`
   - Map link: the user's Google Maps link if they gave one, else `https://www.google.com/maps/search/?api=1&query=<url-encoded name + Philadelphia>`
4. Update the "Ratings checked" date at the bottom if you refresh ratings.
5. Check it at phone width (375px), then commit and push. GitHub Pages redeploys in about 1 minute.
