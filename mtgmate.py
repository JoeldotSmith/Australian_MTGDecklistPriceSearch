import re
import urllib.request
import urllib.parse
from models import CardResult

EXCLUDE_CONDITIONS = {
    "heavily played",
    "damaged",
    "heavily played foil",
    "damaged foil",
}


def fetch_all(cards: list[str]) -> dict[str, CardResult]:
    """
    Fetch all cards in one bulk request to MTGMate.
    Returns:
      results : dict  card_name_lower -> CardResult (cheapest in-stock, excl. bad conditions)
    """
    print(f"  [MTGMate] Fetching {len(cards)} cards (bulk)...", end=" ", flush=True)

    html = _fetch_html(cards)
    if html is None:
        return {}

    results = _parse(html)
    print(f"✓  ({len(results)} found)")
    return results


def _fetch_html(cards: list[str]) -> str | None:
    decklist = "\n".join(f"1 {name}" for name in cards)
    params = urllib.parse.urlencode({"utf8": "✓", "decklist": decklist, "commit": "Build Deck"})
    url = f"https://www.mtgmate.com.au/cards/decklist_results?{params}"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-AU,en;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"\n  [MTGMate] Request failed: {e}")
        return None

def _parse(html: str) -> dict[str, CardResult]:
    results = {}

    # ── Not-found cards ────────────────────────────────────────────────────────
    for li in re.finditer(r'<li class="partially-in-stock">(?:\d+x\s+)?([^<]+)</li>', html):
        pass  # we don't need to track these separately; absence from results is enough

    # ── Split on card-name headers ─────────────────────────────────────────────
    # <th class="card-name text-center" colspan=4>\n  Archmage Emeritus\n</th>
    chunks = re.split(r'<th[^>]*class="card-name[^"]*"[^>]*>\s*([^<]+?)\s*</th>', html)
    # chunks = [preamble, card1_name, card1_html, card2_name, card2_html, ...]

    EXCLUDE = {"heavily played", "damaged", "heavily played foil", "damaged foil"}

    i = 1
    while i + 1 < len(chunks):
        card_key = chunks[i].strip().lower()
        block = chunks[i + 1]
        i += 2

        # Guard: skip anything that looks like it still contains HTML tags
        # (means the split caught a non-card-name th)
        if "<" in card_key:
            continue

        for row in re.finditer(r'<tr class="magic-card[^"]*">(.*?)</tr>', block, re.DOTALL):
            row_html = row.group(1)

            href_match = re.search(r'href="/cards/([^"]+)"', row_html)
            if not href_match:
                continue

            # Condition from URL slug: last colon-separated segment
            slug_match = re.search(r':([a-z-]+)"', row_html)
            condition = slug_match.group(1).replace("-", " ").title() if slug_match else "Unknown"

            if condition.lower() in EXCLUDE:
                continue

            set_match = re.search(r'href="/cards/[^"]+">([^<]+)</a>', row_html)
            set_name = set_match.group(1).strip() if set_match else ""

            # Qty and price may appear in separate tds OR inline in the card-name td
            qty_match = re.search(r'Available:\s*(\d+)', row_html)
            price_match = re.search(r'\$([0-9]+\.[0-9]+)', row_html)

            if not (qty_match and price_match):
                continue

            qty = int(qty_match.group(1))
            price_cents = int(round(float(price_match.group(1)) * 100))

            if qty == 0:
                continue

            href_full = re.search(r'href="(/cards/[^"]+)"', row_html)
            card_url = f"https://www.mtgmate.com.au{href_full.group(1)}" if href_full else None

            if card_key not in results or price_cents < results[card_key].price_cents:
                results[card_key] = CardResult(
                    card_name=chunks[i - 2].strip(),  # correct index: name is 2 behind current i
                    set_name=set_name,
                    condition=condition,
                    qty=qty,
                    price_cents=price_cents,
                    url=card_url,
                )

    return results
