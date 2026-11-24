# Philly Thanksgiving trip page

The whole site is `index.html`. All place data is in the `PLACES` object near the top of its script.

## Adding a place: always add reviews

Every time a place is added, look up and fill in both review sources before publishing:

1. Google: run `python3 -I scripts/google_rating.py "<Place Name> Philadelphia"`. Check that `gname` is the right place, then copy `rating`, `count` and `url` into `google`.
2. TripAdvisor: search `tripadvisor <Place Name> Philadelphia` and take the rating, review count and listing URL from the Philadelphia listing. Use `rating: null, count: 0` when a listing has no reviews. Use `ta: null` when there is no listing. Never guess numbers.
3. Fill in `fri`, `sat` (hours) and `q` (the text the map searches for). Add `link` only if the user gave a Google Maps link.
4. Update the "Ratings checked" date at the bottom of the page if you refresh ratings.
5. Check it at phone width (375px), then commit and push. GitHub Pages redeploys in about 1 minute.
