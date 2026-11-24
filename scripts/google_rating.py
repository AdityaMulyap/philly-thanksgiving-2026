# Usage: python3 scripts/google_rating.py "Place Name Philadelphia" ["Another Place"]
# Prints Google rating, review count and reviews URL, read from the Google Maps embed page.
import re, sys, json, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
out = {}
for q in sys.argv[1:]:
    url = "https://www.google.com/maps/embed?origin=mfe&pb=!1m3!2m1!1s" + urllib.parse.quote_plus(q) + "!6i15"
    html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20).read().decode("utf-8", "replace")
    m = re.search(r'"([^"]+)",\[("[^"]*",?)+\],([0-9.]+),"([\d,]+) reviews?","([^"]+)"', html)
    if m:
        out[q] = {"gname": m.group(1), "rating": round(float(m.group(3)), 1), "count": int(m.group(4).replace(",", "")), "url": m.group(5).encode().decode("unicode_escape")}
    else:
        out[q] = None
print(json.dumps(out, indent=1, ensure_ascii=False))
